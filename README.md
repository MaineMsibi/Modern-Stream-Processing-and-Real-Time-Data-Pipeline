# Modern-Stream-Processing-and-Real-Time-Data-Pipeline\
This project showcases the implementation of a low-latency, cloud-native real-time data pipeline using Azure’s event-driven architecture. It focuses on simulating and ingesting live financial transaction data and processing it through a distributed stream processing engine to derive timely and actionable insights. The pipeline simulates heterogeneous transaction sources and leverages Azure Event Hub for durable, high-throughput ingestion; Azure Stream Analytics for real-time transformation and analytics using a SQL-like query language; and multiple output sinks to serve different business needs. Transactions simulation is generated using a python script.

Specifically, the pipeline writes the streaming data to:
	*Azure Cosmos DB, a globally distributed NoSQL database for storing historical, aggregated transaction data for batch analysis on Power BI.
  *Power BI Service (Streaming Dataset) for real-time dashboarding, this in real life can allow business users to monitor financial activity (e.g., fraud detection, abnormal transaction volumes) as it happens with updates every few seconds.
  
The solution follows modern stream processing paradigms - event-driven design, decoupled data flow, and near-instant visualization - making it ideal for time-sensitive domains like banking and fintech where sub-minute latency and continuous insight generation are mission critical.
By simulating real-world banking operations, this architecture also highlights the power of hybrid analytics, where batch and real-time outputs coexist for complete data observability.
