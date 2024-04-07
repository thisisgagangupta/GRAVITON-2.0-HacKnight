import speech_recognition as sr
from nltk.tokenize import word_tokenize
from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def quantum_inspired_semantic_analysis(text):
    tokens = word_tokenize(text)
    num_qubits = len(tokens)
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    for i, token in enumerate(tokens):
        qc.h(i)  
    
    qc.measure(range(num_qubits), range(num_qubits))
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    counts = result.get_counts()
    
    semantic_analysis_results = {bin(int(k, 2))[2:]: v / 1024 for k, v in counts.items()}
    
    return semantic_analysis_results

audio_file = "extracted_audio.wav" 
transcript = audio_to_text(audio_file)
print(transcript)

semantic_analysis_results = quantum_inspired_semantic_analysis(transcript)
print("Semantic Analysis Results:", semantic_analysis_results)