# 📌 **AI Hand-Gesture Drawing App**

### *A Computer Vision Project Using Python, OpenCV & MediaPipe*

A real-time **AI drawing application** that tracks your **hand gestures through the webcam** and allows you to **draw, erase, and select colors in the air** — completely touch-free.

This project uses **MediaPipe Hand Tracking** + **OpenCV drawing pipeline**, offering an intuitive and interactive way to draw on your screen using just your finger.

---

## 🚀 **Features**

* 🎨 **Air Drawing** — Draw on the screen with your index finger
* 🖐️ **Gesture Control Modes**

  * **Draw Mode:** Only index finger up
  * **Select Mode:** All five fingers open
* 🎨 **Color Selection Panel (Left Side)**

  * Blue
  * Green
  * Red
  * Yellow
* 🧽 **Eraser Tool (Right Side Panel)**

  * Select the “ERASE” panel to switch to erase mode
  * Erases only the touched area (does NOT clear whole canvas)
* 🖼️ **Live Webcam Feed** blended with the drawing canvas
* ⚡ Real-time tracking at high FPS
* 🧠 Accurate finger detection using Machine Learning landmarks

---

## 🧰 **Tech Stack**

* **Python 3.10**
* **OpenCV**
* **MediaPipe**
* **NumPy**

---

## 📂 **Project Structure**

```
hand-drawing-app/
│── app.py
│── README.md
│── /screenshots
```

---

## 🔧 **Installation & Setup**

### 1️⃣ **Create a virtual environment (recommended)**

```bash
python -m venv env
env\Scripts\activate   # Windows
```

### 2️⃣ **Install dependencies**

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ **Run the Application**

```bash
python app.py
```

Your webcam will open automatically.

---

## ✋ **Gestures & Controls**

### 🎨 **Draw Mode**

Pose: ✋ Only **index finger** up
Action: Draws colored lines on the screen.

---

### 🖐️ **Select Mode**

Pose: 🖐️ All five fingers open
Action:

* Choose colors from left panel
* Choose eraser from right panel

---

### 🧽 **Eraser Mode**

* Enter **Select Mode**
* Point to **ERASE panel** on the right
* Switches to eraser
* Erases only where you move your finger (large white stroke)

---

## 🧠 **How It Works (Short Explanation)**

* MediaPipe detects **21 hand landmarks**
* Finger positions determine gesture → mode
* OpenCV creates a transparent **drawing canvas**
* Lines are drawn based on finger motion
* Frame + canvas are merged using `addWeighted()`

---

## 📘 **App Flowchart (Optional to Add as Image)**

```
Webcam → MediaPipe Hand Tracking → Gesture Detection
            ↓
    Draw Mode / Select Mode / Erase Mode
            ↓
      OpenCV Canvas Rendering
```

---

## 💡 **Future Enhancements**

* ✨ Brush Size Control (Pinch Gesture)
* ✨ Undo / Redo
* ✨ Save Canvas as PNG
* ✨ Brush Shape Selector
* ✨ Multicolor gradients
* ✨ GUI with custom buttons (Tkinter / PyQt)

---


---

## 📜 **License**

This project is released under the **MIT License**.
Feel free to modify and use it in your own projects.
