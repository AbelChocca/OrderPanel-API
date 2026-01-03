from dataclasses import dataclass

@dataclass(frozen=True)
class KafkaConfig:
    bootstrap_servers: str
    client_id: str
