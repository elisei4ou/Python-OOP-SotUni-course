from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = [f"{self.name} Main Service:"]

        if self.robots:
            robots_name = [r.name for r in self.robots]
            result.append(f"Robots: {' '.join(robots_name)}")
        else:
            result.append("Robots: none")

        return "\n".join(result)
