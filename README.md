# 📘 **LAB 1 – Introduction à ROS2 (Résumé + Exercices 1→5)**

## 🌟 **Résumé global du Lab 1**

Le Lab 1 introduit les concepts fondamentaux de ROS2 :

* Les **workspaces**
* Les **packages**
* La **communication** via **topics** (pub/sub)
* L'utilisation de **nodes**, **launch files**, et outils de base 

L’objectif principal : comprendre comment deux nœuds communiquent entre eux via un topic, et comment lancer un nœud, vérifier les topics, et interpréter les messages.


# 🟦 **Exercice 1 - Modify the Publisher

**Goal:** Change your publisher to send different messages

**Tasks:**
1. Open `simple_publisher.py` in VS Code
2. Modify to publish your name instead of "Hello ROS2"
3. Change timer to 0.5 seconds
4. Rebuild and test

### 📸 Captures

<img width="442" height="208" alt="image" src="https://github.com/user-attachments/assets/3985f3ef-9aa0-4cfd-b6c0-a0832a3ad580" />
<img width="1045" height="611" alt="image" src="https://github.com/user-attachments/assets/28cea4c9-9790-4974-bc0b-e58604e265d9" />

---

# 🟩 **Exercice 2 - Add Message Counter

**Goal:** Make the subscriber count messages

**Tasks:**
1. Open `simple_subscriber.py` in VS Code
2. Add counter variable in `__init__()`
3. Increment in `listener_callback()`
4. Print total count
5. Rebuild and test

### 📸 Captures

<img width="1580" height="614" alt="image" src="https://github.com/user-attachments/assets/bcf50ac7-079f-402f-bcc9-b65270b2ab09" />
<img width="1580" height="488" alt="image" src="https://github.com/user-attachments/assets/ede52e85-068b-4498-88f7-cfb11041f4cd" />

---

# 🟧 **Exercice 3 - Number Publisher (Medium-Hard)

**Goal:** Create publisher that sends integers

**Tasks:**
1. Create `number_publisher.py` in VS Code
2. Use `std_msgs/msg/Int32`
3. Create `number_subscriber.py` that doubles numbers
4. Update `setup.py` entry points
5. Build and test

### 📸 Captures

<img width="1786" height="516" alt="image" src="https://github.com/user-attachments/assets/d68a8090-3603-49a2-8175-903b23fca7c1" />

---

# 🟥 **Exercice 4 - Turtle Controller (Hard)

**Goal:** Make turtle draw a square

**Tasks:**
1. Create `turtle_square.py`
2. Publish to `/turtle1/cmd_vel`
3. Use `geometry_msgs/msg/Twist`
4. Move forward, turn 90°, repeat 4 times

### 📸 Captures

<img width="1778" height="706" alt="image" src="https://github.com/user-attachments/assets/08b548fc-b519-4711-8399-4d85b62b10cf" />

---

# 🟪 **Exercice 5 - Two-Way Communication (Advanced)

**Goal:** Create a request-response system

**Tasks:**
1. Create `ping_node.py` - publishes "PING" to `/ping_topic`
2. Create `pong_node.py` - subscribes to `/ping_topic`, publishes "PONG" to `/pong_topic`
3. Modify `ping_node` to also subscribe to `/pong_topic`
4. Log the round-trip communication

**Expected output:**
```
[ping_node]: Sent PING #1
[pong_node]: Received PING #1, sending PONG
[ping_node]: Received PONG for PING #1
[ping_node]: Sent PING #2
...
```

**Bonus:** Calculate and display the round-trip time

### 📸 Captures

<img width="1778" height="566" alt="image" src="https://github.com/user-attachments/assets/90d11b00-bcc2-42ad-b0da-99d3e1fcc2a8" />
<img width="1778" height="566" alt="image" src="https://github.com/user-attachments/assets/fe997a06-bd05-4d80-92da-4027c127591c" />

---

# 📝 **Résumé final du Lab 1**

À la fin du Lab 1, on a traiter :

### ✔️ Créer un workspace ROS2

### ✔️ Construire et sourcer ton environnement

### ✔️ Lancer des nœuds existants

### ✔️ Voir et analyser les topics

### ✔️ Publier manuellement des messages

### ✔️ Comprendre les types de messages ROS2

### ✔️ Créer ton premier package et node simple

### ✔️ Vérifier la communication entre ton node et d’autres programmes ROS2

---
<img width="729" height="222" alt="image" src="https://github.com/user-attachments/assets/d2110863-e564-47c7-9b06-0f683f53ae75" />
<img width="375" height="460" alt="image" src="https://github.com/user-attachments/assets/482d53bd-f0ac-45ca-b17d-8c00ed36704c" />
