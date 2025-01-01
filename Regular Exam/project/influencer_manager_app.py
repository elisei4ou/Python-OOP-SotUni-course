from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self.find_obg_by_name(username, self.influencers)
        if influencer:
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self.find_obg_by_id(campaign_id, self.campaigns)
        if campaign:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer: BaseInfluencer = self.find_obg_by_name(influencer_username, self.influencers)
        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign: BaseCampaign = self.find_obg_by_id(campaign_id, self.campaigns)
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria" \
                   f" for the campaign with ID {campaign_id}."

        if influencer.calculate_payment(campaign) > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}
        for cam in self.campaigns:
            total_followers = 0
            for i in cam.approved_influencers:
                total_followers += i.reached_followers(cam.__class__.__name__)
            if total_followers:
                result[cam] = total_followers

        return result

    def influencer_campaign_report(self, username: str):
        influencer: BaseInfluencer = self.find_obg_by_name(username, self.influencers)
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        result = ["$$ Campaign Statistics $$"]

        for c in sorted_campaigns:
            influensers = c.approved_influencers
            followers = 0
            for i in influensers:
                followers += i.reached_followers(c.__class__.__name__)
            result.append(f"  * Brand: {c.brand}, "
                          f"Total influencers: {len(c.approved_influencers)}, "
                          f"Total budget: ${c.budget:.2f}, "
                          f"Total reached followers: {followers}")

        return "\n".join(result)

    def find_obg_by_name(self, name: str, collection: list):
        try:
            return next(filter(lambda x: x.username == name, collection))
        except StopIteration:
            return None

    def find_obg_by_id(self, id, collection: list):
        try:
            return next(filter(lambda x: x.campaign_id == id, collection))
        except StopIteration:
            return None
