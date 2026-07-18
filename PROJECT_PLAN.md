# Real-Time Market Data Streaming Platform

## Project Overview

A production-inspired real-time data engineering platform that ingests cryptocurrency market data from public APIs, streams events through Apache Kafka, processes data using Spark Structured Streaming, validates data quality, stores analytics-ready data in BigQuery, and creates analytical models using dbt.

The goal of this project is to demonstrate modern data engineering practices including event-driven architecture, streaming processing, cloud data warehousing, infrastructure as code, data quality, and CI/CD.

---

# Project Architecture

```
CoinGecko API
      |
      |
Python Producer
      |
      |
Apache Kafka
      |
      |
Spark Structured Streaming
      |
      |
Great Expectations
      |
      |
BigQuery Raw Layer
      |
      |
dbt Transformations
      |
      |
Analytics Data Mart
      |
      |
Dashboard
```

---

# Technology Stack

| Component | Technology |
|---|---|
| Data Source | CoinGecko API |
| Programming Language | Python |
| Message Broker | Apache Kafka |
| Stream Processing | Apache Spark Structured Streaming |
| Data Quality | Great Expectations |
| Data Warehouse | Google BigQuery |
| Transformation | dbt |
| Infrastructure | Terraform |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Visualization | Looker Studio |

---

# Development Roadmap

## Sprint 1 - Project Foundation

### Objective

Set up the project structure, development environment, and prepare the repository for streaming development.

### Completed Tasks

- [x] Created GitHub repository
- [x] Created project folder structure
- [x] Initialized Python virtual environment
- [x] Created requirements.txt
- [x] Added environment configuration template
- [x] Added project documentation
- [x] Initialized Git repository

### Current Status

Completed ✅

---

# Sprint 2 - Kafka Infrastructure

## Objective

Create the local streaming environment using Docker.

### Tasks

- [ ] Configure Kafka using Docker Compose
- [ ] Configure Kafka UI
- [ ] Create Kafka topics
- [ ] Test producer and consumer communication
- [ ] Understand Kafka partitions and offsets

---

# Sprint 3 - API Producer

## Objective

Develop a Python service that extracts cryptocurrency market data and publishes events to Kafka.

### Tasks

- [ ] Integrate CoinGecko API
- [ ] Implement API client
- [ ] Add retry handling
- [ ] Add logging
- [ ] Serialize messages
- [ ] Publish events to Kafka topic

---

# Sprint 4 - Stream Processing

## Objective

Process Kafka events using Spark Structured Streaming.

### Tasks

- [ ] Create Spark streaming application
- [ ] Consume Kafka messages
- [ ] Implement transformations
- [ ] Add window aggregations
- [ ] Configure checkpointing

---

# Sprint 5 - Data Storage

## Objective

Store processed streaming data in BigQuery.

### Tasks

- [ ] Design BigQuery schema
- [ ] Implement streaming writes
- [ ] Create raw data layer
- [ ] Implement partitioning strategy

---

# Sprint 6 - Data Quality

## Objective

Implement automated validation for streaming data.

### Tasks

- [ ] Add Great Expectations
- [ ] Validate schema
- [ ] Check null values
- [ ] Check invalid prices
- [ ] Handle failed records

---

# Sprint 7 - Data Transformation

## Objective

Build analytics-ready models.

### Tasks

- [ ] Setup dbt project
- [ ] Create staging models
- [ ] Create dimension tables
- [ ] Create fact tables
- [ ] Create analytical marts

---

# Sprint 8 - Infrastructure & Deployment

## Objective

Automate infrastructure and deployment.

### Tasks

- [ ] Create Terraform configuration
- [ ] Provision cloud resources
- [ ] Create GitHub Actions workflows
- [ ] Automate testing and deployment

---

# Sprint 9 - Monitoring & Dashboard

## Objective

Monitor pipeline health and visualize streaming insights.

### Tasks

- [ ] Add pipeline monitoring
- [ ] Track Kafka metrics
- [ ] Create dashboard
- [ ] Document architecture

---

# Key Engineering Decisions

## Why Kafka?

Kafka provides a scalable event streaming platform that decouples data producers and consumers.

## Why Spark Structured Streaming?

Spark provides distributed stream processing capabilities and supports fault tolerance through checkpointing.

## Why BigQuery?

BigQuery provides scalable analytical storage and integrates well with cloud-based analytics workflows.

---

# Project Status

Current Phase:

**Sprint 1 Completed ✅**

Next Phase:

**Kafka Infrastructure Setup 🚀**

## Sprint 2 - Kafka Infrastructure

### Completed Tasks

- [x] Configured Apache Kafka using official Kafka Docker image
- [x] Enabled KRaft mode (ZooKeeper-less architecture)
- [x] Configured Kafka broker and controller roles
- [x] Added Kafka UI for cluster monitoring
- [x] Verified Kafka service availability

### Architecture Decision

Kafka was deployed using the official Apache Kafka Docker image with KRaft mode enabled. This approach was selected to align with modern Kafka deployments and avoid ZooKeeper dependency.

# Sprint 2 - Kafka Infrastructure

## Objective

Set up the event streaming infrastructure required for real-time data ingestion.

## Completed Tasks

- [x] Configured Apache Kafka using Docker Compose
- [x] Enabled Kafka KRaft mode (ZooKeeper-less architecture)
- [x] Configured Kafka broker and controller roles
- [x] Exposed Kafka broker on port 9092
- [x] Added Kafka UI for cluster monitoring
- [x] Verified Kafka container health

## Architecture
Python Producer
|
|
Kafka Broker
|
|
Kafka Topics

## Key Learnings

### Kafka Broker

A Kafka broker is a server responsible for storing and serving event streams.

### Kafka Topic

A topic is a logical stream where events are published and consumed.

### KRaft Mode

Kafka KRaft mode allows Kafka to manage metadata internally without requiring ZooKeeper.

## Current Status

Completed ✅

Next Step:

Create Kafka topics and test message publishing.

## Kafka Topic Setup

### Completed Tasks

- [x] Created Kafka topic: `market-price-events`
- [x] Configured topic with 3 partitions
- [x] Verified topic creation using Kafka CLI

### Topic Configuration

Topic Name:
market-price-events


Partitions:
3


Replication Factor:
1


### Purpose

This topic will store real-time cryptocurrency market events produced by the Python API producer.

Example event:

```json
{
  "coin": "bitcoin",
  "symbol": "BTC",
  "price": 118245.54,
  "volume": 34567289012,
  "timestamp": "2026-07-18T15:30:00Z"
}

---

# Now let's understand what you just created

## Kafka Topic

A topic is a named stream of events.

Think of it like a pipeline:

             market-price-events

Event 1 ───────────────►
Event 2 ───────────────►
Event 3 ───────────────►
Event 4 ───────────────►


Kafka does not modify these events.

It stores them in order.

---

# Partitions

You created:

```bash
--partitions 3

So internally Kafka created:

market-price-events

        |
        |
 ┌──────┼──────┐
 │      │      │
 P0     P1     P2

Why?

Because later Spark can read from multiple partitions in parallel:

Kafka

P0 ─────── Spark Worker 1

P1 ─────── Spark Worker 2

P2 ─────── Spark Worker 3

This is how Kafka scales.

----
## Kafka Message Testing

### Completed Tasks

- [x] Started Kafka console producer
- [x] Published test JSON event
- [x] Started Kafka console consumer
- [x] Successfully consumed Kafka message

### Test Event

```json
{
  "coin": "bitcoin",
  "price": 100000,
  "volume": 2500000000
}
Validation

Kafka successfully transferred messages between producer and consumer.

Sprint 2 Status:

Completed ✅


---

# 🎉 Sprint 2 Summary

You learned:

## 1. Kafka Broker

A Kafka broker stores and manages event streams.

Your broker:


localhost:9092


---

## 2. Kafka Topic

Created:


market-price-events


Configuration:


Partitions: 3
Replication Factor: 1


---

## 3. Producer

A producer publishes events:


Producer
|
|
▼
Kafka Topic


---

## 4. Consumer

A consumer reads events:


Kafka Topic
|
|
▼
Consumer


---

# Current Project Architecture

After Sprint 2:

             Docker

          Apache Kafka
              |
              |
    market-price-events topic
              |
              |
      Console Consumer