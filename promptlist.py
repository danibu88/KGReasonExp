evaluation_prompts = [
    {
        "domain": "Healthcare",
        "title": "AI MedBox for Elderly",
        "prompt": (
            "At SimpleHealth, we've identified a groundbreaking opportunity to revolutionize elderly care with our AI-powered MedBox concept. "
            "This device reminds seniors to take their medications and uses AI to analyze health data and make informed suggestions about treatment plans. "
            "It verifies medication intake, automatically reorders supplies, and even flags potential drug interactions. "
            "The system integrates with healthcare providers to adjust prescriptions in real time and offers visual and voice interfaces for accessibility. "
            "Family members can receive alerts and updates, giving them peace of mind while ensuring independence for the elderly. "
            "This AI health assistant goes beyond medication management—it's a personalized care platform. "
            "We believe MedBox can reduce hospital readmissions, improve treatment adherence, and create a smarter healthcare ecosystem for seniors."
        )
    },
    {
        "domain": "Risk Management",
        "title": "AI Safety System for Sawmills",
        "prompt": (
            "At SafetyFirst Lumber, we are developing a real-time safety system that continuously monitors sawmill operations. "
            "Our AI analyzes vibration, load, and usage patterns from machinery sensors to detect early warning signs of equipment failure. "
            "The system autonomously adjusts cleaning and maintenance schedules based on predicted risk zones. "
            "It not only alerts staff to danger but offers preventive recommendations. "
            "This transforms safety from reactive to proactive. "
            "By minimizing downtime and reducing accidents, the AI enables a safer, more efficient work environment. "
            "It can set new industry standards for intelligent risk mitigation in hazardous manufacturing contexts."
        )
    },
    {
        "domain": "Education",
        "title": "Personalized AI Tutor",
        "prompt": (
            "At FutureLearn Academy, we aim to redefine student engagement with a personalized AI tutor. "
            "This virtual tutor adapts to each student’s pace, preferences, and learning gaps using real-time performance analytics. "
            "It can reframe explanations, suggest targeted exercises, and integrate interactive content such as quizzes and simulations. "
            "For teachers, it provides dashboards that highlight which students need support and which topics are underperforming. "
            "Parents receive insights into learning progress and study habits. "
            "The tutor is available 24/7 across devices, ensuring that learning doesn't stop outside the classroom. "
            "We see this as a way to bridge educational inequality and increase learner confidence through continuous, personalized support."
        )
    },
    {
        "domain": "Retail",
        "title": "AI-Driven Dynamic Pricing",
        "prompt": (
            "At ShopSmart, we are launching a dynamic pricing engine that reacts in real time to market changes. "
            "The AI system tracks competitor pricing, customer demand patterns, and inventory levels to suggest optimal price points. "
            "It can run A/B tests and optimize for metrics like conversion rate or profit margin. "
            "The system is designed to support multiple pricing strategies based on product categories and customer segments. "
            "With explainable AI dashboards, retailers can understand and trust the recommendations. "
            "This engine empowers both e-commerce and brick-and-mortar operations to stay competitive and agile in fast-moving markets."
        )
    },
    {
        "domain": "Manufacturing",
        "title": "Predictive Quality Control",
        "prompt": (
            "ProFabTech is building an AI model that detects defects before they happen. "
            "Using real-time sensor and camera data, the system monitors variables such as temperature, vibration, and assembly alignment. "
            "It applies anomaly detection models to predict failures or product defects before they reach the end of the line. "
            "Operators receive alerts and root-cause analysis, enabling rapid correction. "
            "The system can also recommend design changes to reduce recurring defect types. "
            "This transforms quality assurance from reactive checks to proactive intelligence, potentially reducing waste and improving consistency."
        )
    },
    {
        "domain": "Finance",
        "title": "Fraud Detection System",
        "prompt": (
            "At TrustBank, we’re deploying a fraud detection engine that learns behavioral patterns from millions of transactions. "
            "It flags suspicious activities like sudden changes in location, unusual spending, or duplicate transactions. "
            "Using machine learning, the system continuously refines its models and reduces false positives. "
            "It also explains why a transaction is flagged, offering transparency for review teams. "
            "Integration with mobile apps allows real-time alerts and verification requests to customers. "
            "The goal is to protect users without disrupting legitimate activity—making security seamless and intelligent."
        )
    },
    {
        "domain": "Logistics",
        "title": "Smart Fleet Optimization",
        "prompt": (
            "FleetMove is building an AI-powered fleet optimizer that reroutes vehicles in real time. "
            "The system factors in traffic, weather, vehicle type, and delivery urgency to suggest the most efficient route. "
            "It learns from historical data to predict traffic patterns and anticipate delays. "
            "Drivers receive dynamic instructions via mobile devices, and dispatchers have a live dashboard for oversight. "
            "Fuel usage, emissions, and delivery time are tracked and optimized. "
            "This solution aims to reduce operational costs and carbon footprint while improving on-time delivery performance."
        )
    },
    {
        "domain": "Agriculture",
        "title": "Precision Farming AI",
        "prompt": (
            "At AgriEdge, we’re introducing a smart farming assistant that uses AI to recommend crop treatments. "
            "By integrating satellite imagery, soil sensors, and weather data, the system identifies when and where to irrigate, fertilize, or treat for pests. "
            "It provides mobile alerts to farmers and integrates with machinery to automate some actions. "
            "Crop yield forecasts help in planning logistics and sales. "
            "Over time, the AI learns farm-specific conditions and improves its accuracy. "
            "This leads to more sustainable, resource-efficient farming with higher productivity."
        )
    },
    {
        "domain": "Cybersecurity",
        "title": "Autonomous Threat Detection",
        "prompt": (
            "At SafeNet, we’re implementing a cybersecurity AI that detects and responds to network threats autonomously. "
            "It uses pattern recognition to identify anomalies in traffic, login behavior, or API calls. "
            "When a breach is suspected, it can isolate systems, block IPs, and notify admins immediately. "
            "The system learns from emerging threats to keep ahead of zero-day vulnerabilities. "
            "A real-time dashboard offers visibility into system health and ongoing attacks. "
            "This AI acts as both guard and investigator, offering round-the-clock protection without human fatigue."
        )
    },
    {
        "domain": "Legal",
        "title": "Contract Risk Analyzer",
        "prompt": (
            "At LawBotics, we’re designing an AI system to scan legal documents for high-risk clauses. "
            "The system uses NLP and legal domain models to flag vague, biased, or non-compliant sections in contracts. "
            "It suggests alternative phrasings and highlights missing mandatory terms. "
            "Lawyers can review the output and approve edits via a simple interface. "
            "It supports various contract types from NDAs to procurement and licensing agreements. "
            "This tool will save time, reduce litigation risk, and ensure regulatory compliance for firms of all sizes."
        )
    },
    {
        "domain": "Construction",
        "title": "Site Safety Intelligence",
        "prompt": (
            "ConstructAI is developing a real-time visual safety monitor for construction sites. "
            "Using drone and CCTV feeds, the AI identifies workers not wearing PPE, unsafe scaffold usage, and other hazards. "
            "It sends live alerts to site managers and logs incidents with video evidence. "
            "The system tracks safety trends over time and can suggest changes to protocols or training. "
            "With multilingual support, it improves communication with international teams. "
            "This technology ensures compliance and actively prevents workplace injuries."
        )
    },
    {
        "domain": "Hospitality",
        "title": "AI Concierge Assistant",
        "prompt": (
            "At LuxeStay, we are designing an AI-powered concierge that learns guest preferences across multiple visits. "
            "The assistant handles restaurant reservations, service requests, and amenity recommendations in real time. "
            "It adjusts its tone and suggestions based on guest type—business, family, or luxury traveler. "
            "Staff can use the same system for internal coordination, improving service delivery. "
            "This AI not only enhances guest experience but also drives loyalty and operational efficiency."
        )
    },
    {
        "domain": "Telecom",
        "title": "Network Outage Prediction",
        "prompt": (
            "NetWatch is developing a predictive analytics tool for telcos to prevent outages. "
            "The AI models analyze switch logs, signal strength patterns, and user complaints to detect early degradation. "
            "It recommends preemptive rerouting or technician dispatches to avoid customer impact. "
            "Downtime is minimized and SLAs are better maintained. "
            "This innovation could dramatically improve service reliability in densely connected urban zones."
        )
    },
    {
        "domain": "Energy",
        "title": "Smart Grid Balancing",
        "prompt": (
            "At Voltix, we are leveraging AI to balance energy demand and supply in smart grids. "
            "The system forecasts solar and wind generation and adjusts load allocation in real time. "
            "It can also incentivize usage shifts through dynamic pricing models. "
            "Outages are avoided, and renewable penetration is maximized. "
            "This is a foundational technology for the next generation of clean, reliable energy infrastructure."
        )
    }
]
