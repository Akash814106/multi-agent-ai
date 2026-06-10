from backend.agents.worker_agents.summary_agent import summary_agent

revision_output = """
Microservices architecture is an approach where applications
are divided into small independent services.

It includes:
- Service Discovery
- API Gateway
- Docker
- Kubernetes

Benefits include scalability, maintainability,
and independent deployment.
"""

result  = summary_agent(revision_output)
print("\nResult : \n")
print(result)