## Introduction

A common challenge is effectively introducing and managing services, internal and external, while preserving data integrity. With an array of systems and subsystems, there's a need for a streamlined pattern that enhances interoperability without the bottleneck of rigid data structures. The 'adapter-service' pattern addresses this challenge, enhancing how we manage data and services. This article delves into the adapter-service pattern, its interplay with the 'domain object' concept, implicit anti-corruption layers, the messaging data distribution architecture, and its real-world application.

__Goals__

1. Above all else, speed
2. Distribute data efficiently between internal and external systems
3. Ability to introduce new services, internal and external rapidly
4. Distribute risk and criticality across more services
5. Enable swift changes in business logic

## Understanding the adapter-service pattern

The adapter+service pattern, underpinned by the 'domain object' concept and its implicit anti-corruption layer, is a design approach aimed at making system integration and data distribution more flexible and efficient. 

## Fundamental elements

### Services

#### Internal microservices
These are the operational units, including microservices, that generate and consume data. Services subscribe to 'domain objects', either partially or fully, distribute new messages with enriched content and ensure data flow within the system.

Sometimes thought of as anti-pattern, multiple services can co-exist within a single domain. As described in <insert reference

#### External SaaS

### Adapters / integrations

These serve as the communication interface between different services and applications, both internal and external. Adapters define their required fields for distributing data to the external services based on the 'domain objects'.

These are effective at receiving and sending data in external service proprietary formats, you can even support file integrations, robotics process automation, webhooks, and really any form of integration or external service.
The strength of the adapter-service pattern lies in its adaptability and flexibility, which enable it to cater to a diverse range of business requirements. The only mandatory field for any 'domain object' is the unique identifier (ID), which allows for the partial or complete distribution of 'domain objects' across different services through adapters.


#### Implementation
2. Adapters are clearly defined within domains

### Data distribution
Anything can sub and pub messages, they are all "events" meaning they have happened. 

#### Ledger
The services and adapters reads from the ledger in a somewhat way in a propriatery way
1. Latest `state` is always read, by combining the messages by `entityId` 
2. All `null` values are omitted 

The strength of the adapter+service pattern lies in its flexibility and ability to adapt to a variety of business requirements. The only mandatory field for any 'domain object' is the unique identifier (ID), which allows partial or complete distribution of 'domain objects' across different services through the adapters.

## Applying the Adapter+Service Pattern in Real-World Scenarios

The efficacy of the adapter-service pattern becomes abundantly clear when applied to real-world business scenarios. Take for example a global eCommerce platform with various microservices such as user management, inventory control, payment processing, and shipment tracking. In this context, each 'domain object'—be it a user, product, payment, or shipment— can be considered a unit of data distributed across different services via respective adapters.

For instance, the user management service might only require basic user details, while the inventory control service might need detailed product information. The shipment tracking might have multiple vendors for last mile tracking, which all have to be displayed and tracked in the same data model. The 'domain object' approach, facilitated by the adapter-service pattern, allows each service to subscribe to and distribute only the data they require, thereby promoting efficient data management and streamlined operations. Enabling us to introduce new external shipment tracking systems.

Another awesome example is a company looking at M&A candidates, their systems do not have to be changed out in one full sweep of all services, rather you can integrate the company partially and in stages.

Furthermore, external services can interface with the platform via adapters that define and distribute only the necessary fields from each 'domain object'. This preserves data integrity and ensures smooth integration.

## Conclusion

In today's fast-paced business environment, the 'adapter-service' pattern offers a simplified approach to complex system integrations. By leveraging the 'domain object' concept, it provides a standardized and efficient approach to data management, fostering seamless interactions between various systems and services.

The adaptability of the adapter-service pattern enables its adoption across numerous industries, allowing businesses to achieve a high degree of interoperability while preserving data integrity. Remember, in a world where data is the operational lifeblood, efficient data management is not a luxury—it's a necessity. As the saying goes, "we're not saving the planet, we're saving ourselves from a shitty future. Get to work."


