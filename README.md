# <h1 style="font-size: 36px;">EduPrep AI 🤖</h1>

<p align="center">
  <img src="https://github.com/thisisgagangupta/EduPrepAI/assets/93258623/270fe776-a702-4143-8b8e-c444239b90f3" width="680" height="430">
</p>

---

## Problem Research 📚

We conducted extensive research and found that students often struggle to find relevant practice questions, leading to a lack of practice, while teachers face challenges in creating personalized content. Students tend to rely on summary videos for exam preparation, which may not sufficiently cover the material. To address these issues, we propose a solution that offers quick summarization, interactive quizzes, and personalized content generation based on educational videos.


## Problem Statement 🎯

- Watching lengthy lecture videos is time-consuming and tedious.
- Students struggle to find relevant questions for practice.
- Teachers spend considerable time creating quizzes and notes manually.
- Limited access to personalized content affects students' exam preparation.

---

## Solution Overview 💡

Our innovative EdTech platform aims to enhance the learning experience by converting educational video lectures into summary, lecture notes and engaging MCQ-based quizzes and providing automatic assessment. This project not only streamlines the quiz creation process for teachers but also offers students a dynamic and interactive learning environment. With features such as instant grading and performance analytics, our platform facilitates efficient and effective learning.

### Key Features:
- Quick Summarization of Educational Videos
- Interactive Quizzes Based on Video Content
- Automatic Assessment and Performance Analytics

---

## Future Additions 🚀

- AI-generated Notes From PDFs, PowerPoints, and Lecture Videos
- AI Tutor Chat Support for Studying
- Search Functionality within Lecture Videos
- Improved Quiz Generation Algorithms

---

## Roadmap 🛣️

1. **Scraping Data** [Successful]

2. **Data Collection and Selection** [Successful]
    - Utilize educational videos from open access university websites and YouTube

3. **Frame Extraction** [Successful]
    - Extract frames using ffmpeg

4. **Labeling Dataset** [Successful]
    - Label frames as slide, presenter slide, and others

5. **Model Training**
    - Base Models: Resnet50, YOLO, EAST, LLama2-7b
    - Future Scope: Explore state-of-the-art models

6. **Image Tuning Operations** [Successful]
    - Crop Transform, Border Removal, Segment Clustering, Image Hashing

7. **Sequential Data Context Search Training** [Successful]

8. **OCR, Figure Detection** [Ongoing]

9. **Transcription (Multimodal)**
    - Audio to Transcript Generation

10. **Combination and Sync**

11. **Text Operations**
    - Spell Check, etc.

12. **Summarization and Quiz Generation**
    - Utilize LLama2 finetuning and pre-existing models like BERT-edu
    - Answer Key/Options Generation using Sense2vec word vectors
   
13. **Chat with Video**

---

## Use Cases ✨

### Multimodal and Multilingual Approach
### Quick Summarization of Lecture Videos
### Interactive Quizzes to Enhance Learning and Practice
### Personalized Content based on Lecture Topics
### Customizable Question Types and Parameters
### Saves Time and Efforts (can be used as a browser extension)

---

## Future Scope 🔭

- Incorporate Natural Language Understanding (NLU) models for assessment
- Database Integration for improved efficiency
- Enhanced Security measures for user data protection
- Development of an internal AI assistant for navigation

---

For detailed implementation and updates, please visit [EduPrepAI GitHub Repository](https://github.com/thisisgagangupta/EduPrepAI).
