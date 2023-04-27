# Anarchy as system architecture

In an ever-evolving tech landscape, businesses need flexible and scalable system architectures to stay ahead. Anarchy as a system architecture offers a unique approach to achieving this. Inspired by the principles of Clean Architecture by Robert C. Martin, this model emphasizes a decentralized and flexible framework where components are connected through a messaging system. In this architecture, services can freely subscribe and publish to the message bus, fostering adaptability and resilience.

## Messaging system
A robust message bus allows components to subscribe and publish, enabling easy communication and coordination between services 📨

## Functions for reading and writing to topics
Standardizing the reading and writing of topics through general utility functions ensures a consistent approach, making a complex archtecture easier to work with for all parties. 
### Getting a message
```
messaging.get(client, entityId)
```
### Posting a message
```
messaging.post(client, topic, {
  // message content
})
```

## External system adapters
Each adapter is dedicated to a single topic, ensuring clean and modular connections between external systems and the message bus. This approach requires multiple adapters for systems that interact with multiple topics, promoting separation of concerns 🔌

Adapters should not maintain their own state, further reducing complexity and ensuring the messaging system remains the primary source of truth

## Microservices

### Localized data storage
Each service maintains its own database for all its required information, ensuring that data is stored and managed efficiently and independently.

Embracing anarchy as a system architecture can lead to increased flexibility, adaptability, and scalability. The decentralized nature of this approach encourages services to operate autonomously while still benefiting from a shared messaging system. This ultimately enables teams to build more resilient, modular, and adaptable systems, ready to tackle the challenges of the rapidly evolving technology landscape.
