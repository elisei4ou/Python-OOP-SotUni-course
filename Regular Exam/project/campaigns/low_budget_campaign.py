from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, required_engagement=required_engagement, budget=self.BUDGET)

    def check_eligibility(self, engagement_rate: float):
        return self.required_engagement * 0.9 <= engagement_rate
