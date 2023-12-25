from dataclasses import dataclass


@dataclass
class student:
    names: str
    ids: int
    emails: str

    def get_details(self):
        print(f"{self.names}\n{self.ids}\n{self.emails}")
        print("=" *40)
