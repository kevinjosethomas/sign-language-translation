Introduction
American Sign Language (ASL) is a rich, fully developed natural language—distinct from English in its grammar and culture. Inspired by firsthand observations at university and competitive research in computer vision, this project addresses the limitations of conventional translation tools, aiming to deliver meaningful two-way communication for both signers and non-signers. The interface offers:

ASL Fingerspelling → English	English → ASL Sign
Converts ASL fingerspelling directly into English text (and speech), opening smoother communication for Deaf and Hard-of-Hearing users.	Translates spoken English into animated ASL signs via a web-based avatar, improving accessibility and engagement for signers.
Motivation
Driven by coursework and personal curiosity about how technology supports accessibility, this project reflects a desire to go beyond surface-level translation solutions. Existing tools often overlook the linguistic uniqueness of ASL and the lived experiences of its speakers. Combining insights from soft computing and machine learning courses, the prototype aims to respect ASL’s visual grammar and bridge communication gaps in real settings.

Technology Overview
This modular project integrates:

Computer vision & gesture tracking (MediaPipe)

3D point-cloud gesture recognition (PointNet in Tensorflow/Keras)

Web-based avatar animation (ThreeJS)

Semantic vector embeddings (MiniLM and PostgreSQL pgvector)

Core Features:
Receptive (ASL → English): Deciphers hand landmarks with PointNet, synthesizing fluent English from gesture streams.

Expressive (English → ASL): Translates spoken English input and animates ASL via avatar using pose data and embeddings.

Design Principles
Reflecting on how translation tools traditionally center hearing conventions, this project is designed to prioritize ASL-native grammar and visual communication. The gesture recognition pipeline focuses on ASL’s five linguistic parameters: handshape, movement, location, palm orientation, and non-manual markers, striving for robust performance across diverse users and physical backgrounds.

Training & Implementation
ASL alphabet datasets sourced from open platforms (Kaggle) and normalized hand landmarks via MediaPipe.

Data augmentation and point-cloud preparation for noise tolerance.

Model development using PointNet, with continuous gestures refined using LLM-based error correction to generate coherent English output.

System Flow
Detect and track hand landmarks (MediaPipe: 21 points per frame)

Point cloud normalization and gesture classification (PointNet model)

Output synthesis and error correction for English translation

For English input, speech is transcribed, mapped to ASL embedding space, and animated with an avatar in-browser

Limitations & Future Directions
At present, the system specializes in fingerspelling and basic signs; planned upgrades include full ASL sentence modeling with LSTM/Transformer architectures.

Avatar animations currently lack non-manual features (facial, two-handed, posture).

Upcoming research will focus on richer expressiveness, domain adaptation, and multi-modal fusion.

Acknowledgements
Gratitude to educators, fellow students, and the accessibility community for technical feedback and inspiration. Special thanks to open-source projects and course mentors for foundational resources, and to university collaborators for ongoing support.

How to Run
[Update with step-by-step install, setup, and usage instructions tailored to your workflow and environment]

Replace generic acknowledgements, contacts, and instructions with your own details, university, and collaborators.

Ensure your personal statement and workflow descriptions are visible.

Customize the license to reflect your name or preferred terms for open-source distribution.
