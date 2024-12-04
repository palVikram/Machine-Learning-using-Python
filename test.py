Introduction:
The objective of this project is to develop a scalable and adaptable solution for content moderation that can address diverse prompt definitions tailored to specific client requirements. The aim is to build a real-time classifier capable of processing and categorizing various types of prompts or policies (e.g., violence, hate speech) for a single topic, thereby enabling proactive and effective content moderation across platforms.

Problem Statement:
The Mistral 7B model, with 7 billion parameters in FP16 (half-precision), has a substantial model size of 15 GB, where each parameter requires 2 bytes of memory. This poses challenges in terms of efficient deployment and resource utilization.

High inference latency is a critical concern, as the current latency levels are unsuitable for proactive content moderation tasks. The target latency for real-time classification needs to be under 100 milliseconds.

Handling large prompt input tokens efficiently is crucial to maintain accuracy and responsiveness in content classification.
