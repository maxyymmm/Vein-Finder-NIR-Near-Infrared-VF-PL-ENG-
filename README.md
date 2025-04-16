# ENG BELOW! <br> <br>
# 🔬 Skaner Żył NIR (Near-Infrared)  (VF)
### 📊 WYNIKI
#### Obraz zarejestrowany przez kamere NoIR
![ori](https://user-images.githubusercontent.com/120425774/219521156-9f1e4441-8b21-4a45-9fe9-f68e8397a692.jpg)
#### CLAHE
![CLAHE_samo](https://user-images.githubusercontent.com/120425774/219521268-9f01fa3c-147e-4599-993e-a9984521db71.jpg)
#### CLAHE + Median Filter
![CLAHE MEDIAN](https://user-images.githubusercontent.com/120425774/219521323-53cdf4f9-16bd-412f-8ff5-160d1b7c01ad.jpg)


https://github.com/user-attachments/assets/bc7ac4bf-a98d-4c4a-9d43-718a29301329


https://github.com/user-attachments/assets/aef5d5cf-615a-48e7-bf75-2db40421cf0e

#### 📱 Widok w aplikacji
![app10000](https://github.com/user-attachments/assets/ecc1131b-3af2-4c46-a15d-ad3759651756)
## 🎛️ Parametry sterowalne z aplikacji:
+ 🔁 **Liczba iteracji (for_value)** – Określa, ile razy poprawa kontrastu (CLAHE) jest stosowana. Więcej iteracji może zwiększyć widoczność żył, ale może też dodać szumy, a także znacznie spowolnić pracę urządzenia

+ 🌗 **Limit kontrastu (cliplimit_value)** – Kontroluje, jak mocno wzmacniany jest kontrast. Niższe wartości dają delikatniejsze efekty, wyższe mogą uwypuklić żyły, ale czasem pogarszają jakość obrazu.

+ 🔳 **Rozmiar siatki (tilegrid_value)** – Decyduje, na jak małe fragmenty dzielony jest obraz przy poprawie kontrastu. Większa siatka oznacza bardziej lokalne dostosowanie kontrastu.

+ 🔎 **Rozdzielczość (resolution)** – Ustawia rozdzielczość kamery.

![IMG_7726](https://github.com/user-attachments/assets/3f088ef8-7a82-422d-8c78-68bf12235169)
![IMG_7730](https://github.com/user-attachments/assets/8aa85288-94c9-4dd6-9bdb-b27701fad189)
![IMG_7728](https://github.com/user-attachments/assets/26df9d3f-5bf8-40c7-a73e-9dbeecb5d2ef)
![IMG_7737](https://github.com/user-attachments/assets/4184b829-ff62-49e5-99b6-1065cf47ad8f)
![IMG_7736](https://github.com/user-attachments/assets/35be0645-4171-4fb2-961b-b118ae69cdf3)
![IMG_7716](https://github.com/user-attachments/assets/b6fc7786-ab9b-4a2d-bd0a-7e5b0bd06321)
![IMG_7721](https://github.com/user-attachments/assets/db448214-35a1-4b2d-b4e5-6029c48046ae)

### 🎯 Cel?
Celem tego projektu było stworzenie **przenośnego urządzenia do wizualizacji żył podskórnych w czasie rzeczywistym**, który będzie dostępny za znacznie niższą cenę niż obecnie dostępne profesjonalne urządzenia tego typu, których ceny zaczynają się od **3000$**. **Wykorzystano gotowe i łatwo dostępne do kupienia komponenty, aby zapewnić rozwiązanie jak najbardziej ekonomiczne i stosunkowo proste do samodzielnego złożenia.**
### ❓ Po co to wszystko?
Istnieją grupy chorych, dla których regularne przyjmowanie leków dożylnie (co 2/3 dni) stanowi konieczność, np. w przypadku chorób układu krzepnięcia. **Skaner żył jest narzędziem, które pomaga zminimalizować liczbę koniecznych wkłuć**, dzięki czemu można zmniejszyć niepotrzebny stres i ból dla pacjenta oraz zminimalizować liczbę prób, co jest szczególnie ważne w przypadku niemowląt i dzieci.
### ⚙️ Jak to działa?

![new_scheme](https://github.com/user-attachments/assets/0341a5ab-ce8c-4a20-8f41-206fefdd04e3)



🔬 **Skaner żył** to urządzenie, które wykorzystuje technologię **bliskiej podczerwieni _(NIR, ang. Near-InfraRed)_**, aby zobrazować żyły ukryte pod skórą pacjenta. 
Skaner żył działa w sposób następujący: urządzenie emituje bezpieczne dla organizmu fale podczerwone o długości fal w zakresie **700nm-1000nm _(w tym przypadku 850nm)_**, które przenikają przez skórę pacjenta. W momencie, gdy fale podczerwone trafiają na żyłę, zostają częściowo pochłonięte przez krew, a otaczające tkanki odbijają światło z powrotem. **_Zastosowanie kilku diod o różnych długościach fali może dać nieznacznie lepsze rezultaty, jednak nie ma gotowych układów pozwalających na taką funkcjonalność. Zbudowanie takiego skanera wymagałoby lutowania, stosowania oddzielnych źródeł napięcia i byłoby bardziej skomplikowane. Celem tego projektu było stworzenie stosunkowo prostego urządzenia, które spełnia swoje podstawowe funkcje w bezpieczny i skuteczny sposób._** <br>
W ten sposób kamera pozbawiona filtra **IR _(NoIR camera = No Infrared filter camera)_** rejestruje obraz, który następnie jest przetwarzany przez algorytm **CLAHE _(ang. Contrast Limited Adaptive Histogram Equalization)_** w celu podwyższenia kontrastu. 
Proces przetwarzania obejmuje następujące kroki: <br>
1️⃣ Konwersja obrazu do przestrzeni **barw LAB**.<br>
2️⃣ Zastosowanie **CLAHE** na kanale **L** **_(jasność)_**.<br>
3️⃣ Połączenie kanałów **LAB** z powrotem do obrazu **BGR**.<br>
4️⃣ Na obraz nakładany jest **filtr** **_(Median Filter)_**.<br>
Po przetworzeniu obrazu, jest on wysyłany na lokalny serwer **Flask** działający na urządzeniu. Aby zobaczyć strumień wideo ze skanera żył na innym urządzeniu, należy podłączyć się do hotspotu lokalnego Raspberry Pi. Następnie w przeglądarce internetowej wpisać **"veinfinder.local"** lub **"veinfinder.lan"** , ponieważ jest ustawiony **DNS**. Czasami jednak nie działa on w niektórych przeglądarkach – w takim przypadku należy wpisać adres IP Raspberry Pi: **"http://192.168.1.254/"** lub **"http://192.168.1.254:80"**
Urządzenie zostało wyposażone w baterię o pojemności **3000mah**, która pozwala na kilkanaście minut pracy.

### 🛠️ Sprzęt
💻 **Raspberry pi 4B 4GB**<br>
![raspberry](https://user-images.githubusercontent.com/120425774/219519043-36ef3765-eb90-4844-9529-c078ed58def6.jpg)<br>
📸 **Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)** <br>
![kamera](https://user-images.githubusercontent.com/120425774/219519215-5b22be91-8f97-4141-aab5-ef4c1bae8114.jpg)<br>
🔋 **WaveShare Li-polymer Battery HAT** <br>
![bateria](https://github.com/maxyymmm/Vein-Finder-NIR-Near-Infrared-VF-PL-ENG-/assets/120425774/1bdd070a-82a8-4d7a-826d-7218819fd7f9)<br>
💾 **Karta microSD** <br>
![karta](https://github.com/maxyymmm/Vein-Finder-NIR-Near-Infrared-VF-PL-ENG-/assets/120425774/bd93f27c-4dbc-4471-b82e-a97724ddabe4)<br>
📦 **Obudowa** _(zaprojektowana w Fusion, należy wysłać pliki **.stl** do wydruku 3d)_ <br>

![fusion](https://github.com/user-attachments/assets/c3558dc1-5762-4d31-82d8-f50b1b0a34e0)
![cura](https://github.com/user-attachments/assets/10707d7a-b9f7-40d5-baee-bcaf4782ca82)

### 💵 Koszty:
💻 Raspberry Pi 4B 4GB - **280 PLN** <br>
📸 Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm) - **100 PLN** <br>
🔋 WaveShare Li-polymer Battery HAT - **90 PLN** <br>
💾 Karta microSD - **20 PLN** <br>
📦 Obudowa - Koszt wydruku ok **100 PLN** <br>
   **RAZEM ok 590 PLN**

### 📋 Wymagania
+ Raspberry Pi z zainstalowanym **Raspberry Pi OS (Legacy) 64-bit, 11 (bullseye), Kernel version: 6.1, Release date: October 22nd 2024**.

+ **Python** w wersji **3.9.2**.

### 🛠️ Konfiguracja Raspberry Pi
1️⃣ Pobranie plików z repozytorium na raspberry pi <br>
2️⃣ Instalacja potrzebnych bibliotek z pliku _**requirements.txt**_

Należy przejść do katalogu z pobranymi plikami i wpisać poniższą komendę: 
```console
veinfinder@veinfinder:~$ pip install -r requirements.txt
```

3️⃣ Utworzenie hotspotu **Wifi** + **DNS**
```console
veinfinder@veinfinder:~$ sudo apt update
veinfinder@veinfinder:~$ sudo apt install hostapd dnsmasq
```
![upadte](https://github.com/user-attachments/assets/b7a6e042-0657-4b7c-aadf-5bac396115c5)
```console
veinfinder@veinfinder:~$ sudo systemctl stop hostapd.service
veinfinder@veinfinder:~$ sudo systemctl stop dnsmasq.service
```
```console
veinfinder@veinfinder:~$ sudo nano /etc/dhcpcd.conf
```
![nanoDhcpcd](https://github.com/user-attachments/assets/d55f664e-44f7-48f4-9ddf-9a559562ac19)

Na końcu pliku należy dodać:
```console
interface wlan0
static ip_address=192.168.1.254/24
nohook wpa_supplicant
```
![dhcpcfConf](https://github.com/user-attachments/assets/7ca19b8d-d14d-4894-adcd-490ff736356b)
```console
veinfinder@veinfinder:~$ sudo systemctl restart dhcpcd.service
```
```console
veinfinder@veinfinder:~$ sudo nano /etc/dnsmasq.conf
```
![nanoDns](https://github.com/user-attachments/assets/7b0149ea-94d1-4d69-879d-51a4b6f19b8e)

Na końcu pliku należy dodać:
```console
interface=wlan0
dhcp-range=192.168.1.10,192.168.4.50,255.255.255.0,24h
address=/veinfinder/192.168.1.254
```
![dnsConf](https://github.com/user-attachments/assets/ba352c20-f706-4174-8923-d4e2cd386aae)

```console
veinfinder@veinfinder:~$ sudo systemctl restart dnsmasq.service
```
```console
veinfinder@veinfinder:~$ sudo nano /etc/hostapd/hostapd.conf
```
![hostapdConf](https://github.com/user-attachments/assets/b4956dc2-e1d8-4c37-99c3-a679078ff8ce)

Należy wpisać w pliku:
```console
interface=wlan0
driver=nl80211
ssid=veinfinder
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=0
```
![hostapdConf2](https://github.com/user-attachments/assets/50bab076-257b-4539-889b-cf970107cbe2)

```console
veinfinder@veinfinder:~$ sudo nano /etc/default/hostapd
```
![nanoHostapd](https://github.com/user-attachments/assets/216693ec-5f70-4c62-b08e-558c90063556)
```console
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```
Należy odnaleźć, odkomentować _**(usunąć znak "#")**_ i podać ścieżkę do pliku konfiguracyjnego. Powinno wyglądać to jak poniżej:
![hostapdDeamon](https://github.com/user-attachments/assets/4119c998-4046-43ae-99f2-4af016eb99fc)

```console
veinfinder@veinfinder:~$ sudo systemctl unmask hostapd
veinfinder@veinfinder:~$ sudo systemctl enable hostapd
veinfinder@veinfinder:~$ sudo systemctl start hostapd.service
```
Po wpisaniu:
```console
veinfinder@veinfinder:~$ sudo systemctl status hostapd
```
Powinna wyświetlić się podobna odpowiedź ze statusem **"active"**
![hostapdStatus2](https://github.com/user-attachments/assets/a3b2d7cb-4f9b-4fca-a00b-b7eeea2c8ef3)


4️⃣ Ustawienie automatycznego włączania programu przy starcie urządzenia _**app.py**_
```console
veinfinder@veinfinder:~$ sudo nano /etc/rc.local
```
![rclocal1](https://github.com/user-attachments/assets/ba9a0143-62c0-44bf-9e0d-09af27a70fec)

Należy dopisać na końcu, ale **przed** "exit 0": 
```console
sudo python3 SCIEŻKA_PLIKU/app.py &
```
W tym przypadku:
```console
sudo python3 /home/veinfinder/Desktop/Veinfinder/app.py &
```
![rclocal2](https://github.com/user-attachments/assets/f5397edf-acf6-47d1-87d5-9f204c1c0271)

5️⃣ Dla uzyskania lepszej wydajności można wyłączyć bluetooth oraz włączyć tryb konsolowy

*Wyłączenie bluetooth*
```console
sudo nano /boot/config.txt
```
![turnOffBluetooth](https://github.com/user-attachments/assets/45ce6797-daef-42af-b69f-b0f11628796f)

Należy wpisać na końcu pliku:
```console
dtoverlay=disable-bt
```
![turnOffBluetooth2](https://github.com/user-attachments/assets/2fb94867-1a41-4351-9a5b-497a54de86ae)

*Włączenie trybu konsolowego* 
```console
sudo raspi-config
```
![raspiconfig1](https://github.com/user-attachments/assets/a0e7d2a5-7848-4127-bcb4-2b11ba810962)

_*"System Options -> Boot / Auto Login Select boot... -> Console Autologin..."*_
![raspiconfig2](https://github.com/user-attachments/assets/4fd2fa95-dcb5-454a-a008-00765b29e31f)
![raspiconfig3](https://github.com/user-attachments/assets/e6f04bad-6b5e-4bc2-b5cc-6d20fed2e34d)
![raspiconfig4](https://github.com/user-attachments/assets/fbb8b272-0c7b-4fd4-95ad-99a471cfa3b2)

✅ **GOTOWE!**

### ▶️ Użytkowanie
Urządzenie włączamy przyciskiem **ON/OFF** <br>
Urządzenie wyłączamy naciskając dwukrotnie przycisk **ON/OFF** <br>
Urządzenie można ładować za pomocą **USB TYP C (wspierane szybkie ładowanie)** (5 diod LED wskazuje poziomu naładowania baterii oraz statusu ładowania) <br> <br>

# ENG
# 🔬 Vein Finder NIR (Near-Infrared) (VF)
### 📊 RESULTS
#### Image captured by NoIR camera
![ori](https://user-images.githubusercontent.com/120425774/219521156-9f1e4441-8b21-4a45-9fe9-f68e8397a692.jpg)
#### CLAHE
![CLAHE_samo](https://user-images.githubusercontent.com/120425774/219521268-9f01fa3c-147e-4599-993e-a9984521db71.jpg)
#### CLAHE + Median Filter
![CLAHE MEDIAN](https://user-images.githubusercontent.com/120425774/219521323-53cdf4f9-16bd-412f-8ff5-160d1b7c01ad.jpg)




https://github.com/user-attachments/assets/bc7ac4bf-a98d-4c4a-9d43-718a29301329


https://github.com/user-attachments/assets/aef5d5cf-615a-48e7-bf75-2db40421cf0e

#### 📱 View in the Application
![app10000](https://github.com/user-attachments/assets/ecc1131b-3af2-4c46-a15d-ad3759651756)
## 🎛️ Parameters Adjustable from the Application:
+ 🔁 **Number of Iterations (for_value)** – Controls how many times the CLAHE contrast enhancement process is repeated. More iterations may improve vein visibility but can also add noise and significantly slow down the device.

+ 🌗 **Contrast Limit (cliplimit_value)** – Controls how strongly the contrast is enhanced. Lower values result in a more subtle contrast enhancement, while higher values can make veins more visible but may also degrade image quality

+ 🔳 **Grid Size (tilegrid_value)** – Defines how small the image is divided into sections for contrast enhancement. A larger grid means more localized contrast adjustments.

+ 🔎 **Resolution (resolution)** – Sets the camera resolution.

![IMG_7726](https://github.com/user-attachments/assets/3f088ef8-7a82-422d-8c78-68bf12235169)
![IMG_7730](https://github.com/user-attachments/assets/8aa85288-94c9-4dd6-9bdb-b27701fad189)
![IMG_7728](https://github.com/user-attachments/assets/26df9d3f-5bf8-40c7-a73e-9dbeecb5d2ef)
![IMG_7737](https://github.com/user-attachments/assets/4184b829-ff62-49e5-99b6-1065cf47ad8f)
![IMG_7736](https://github.com/user-attachments/assets/35be0645-4171-4fb2-961b-b118ae69cdf3)
![IMG_7716](https://github.com/user-attachments/assets/b6fc7786-ab9b-4a2d-bd0a-7e5b0bd06321)
![IMG_7721](https://github.com/user-attachments/assets/db448214-35a1-4b2d-b4e5-6029c48046ae)






### 🎯 Purpose?
The aim of this project was to create a **portable device for visualizing subcutaneous veins in real-time**, which would be available at a much lower cost than currently available professional devices of this type, which start at **$3000**. **Ready-made and easily accessible components were used to provide the most economical and relatively simple solution for self-assembly.**
### ❓ Why all this?
There are groups of patients for whom regular intravenous drug administration (every 2/3 days) is necessary, e.g., in the case of coagulation system disorders. **Vein finder is a tool that helps minimize the number of necessary punctures**, thus reducing unnecessary stress and pain for the patient and minimizing the number of attempts, which is particularly important for infants and children.
### ⚙️ How does it work?
![new_scheme](https://github.com/user-attachments/assets/0341a5ab-ce8c-4a20-8f41-206fefdd04e3)


🔬 **Vein scanner** is a device that uses **near-infrared technology (NIR)** to visualize veins hidden under the patient's skin. The vein scanner works as follows: the device emits safe infrared waves with wavelengths in the range of **700nm-1000nm _(in this case 850nm)_**, which penetrate the patient's skin. When the infrared waves hit the vein, they are partially absorbed by the blood, and the surrounding tissues reflect the light back. **_The use of several diodes with different wavelengths may give slightly better results, but there are no ready-made circuits that allow for such functionality. Building such a scanner would require soldering, separate voltage sources, and would be more complicated than what has been achieved in this project. The goal of this project was to create a relatively simple device that fulfills its basic functions in a safe and effective way._** <br>
The camera that is devoid of an **IR filter _(NoIR camera = No Infrared filter camera)_**, records the image, which is then processed by the **CLAHE algorithm _(Contrast Limited Adaptive Histogram Equalization)_** to enhance the contrast.
The processing process involves the following steps: <br>
1️⃣ Conversion of the image to the **LAB color space**.<br>
2️⃣ Applying **CLAHE** to the **L channel _(Lightness)_**.<br>
3️⃣ Merging the **LAB channels** back to the **BGR** image.<br>
4️⃣ A **filter (Median Filter)** is applied to the image.<br>
After processing the image, it is sent to a local **Flask** server running on the device.  
To view the video stream from the vein scanner on another device, connect to the Raspberry Pi's local hotspot.  
Then, open a web browser and enter **"veinfinder.local"** or **"veinfinder.lan"** as the **DNS** is set up.  
However, it may not work in some browsers – in that case, enter the Raspberry Pi's IP address: **"http://192.168.1.254/"** or **"http://192.168.1.254:80"**  

The device is equipped with a **3000mAh** battery, allowing for several minutes of operation.
### 🛠️ Hardware
💻 **Raspberry Pi 4B 4GB**<br>
![raspberry](https://user-images.githubusercontent.com/120425774/219519043-36ef3765-eb90-4844-9529-c078ed58def6.jpg)<br>
📸 **OdSeven Camera HD IR-CUT OV5647 5Mpx + IR modules (850nm)** <br>
![kamera](https://user-images.githubusercontent.com/120425774/219519215-5b22be91-8f97-4141-aab5-ef4c1bae8114.jpg)<br>
🔋 **WaveShare Li-polymer Battery HAT** <br>
![bateria](https://github.com/maxyymmm/Vein-Finder-NIR-Near-Infrared-VF-PL-ENG-/assets/120425774/1bdd070a-82a8-4d7a-826d-7218819fd7f9)<br>
💾 **MicroSD Card** <br>
![karta](https://github.com/maxyymmm/Vein-Finder-NIR-Near-Infrared-VF-PL-ENG-/assets/120425774/bd93f27c-4dbc-4471-b82e-a97724ddabe4)<br>
📦 **Case** _(designed in Fusion, **.stl** files need to be sent for 3d printing)_ <br>
![fusion](https://github.com/user-attachments/assets/c3558dc1-5762-4d31-82d8-f50b1b0a34e0)
![cura](https://github.com/user-attachments/assets/10707d7a-b9f7-40d5-baee-bcaf4782ca82)

### 💵 Costs:
💻 Raspberry pi 4B 4GB - **280zł** <br>
📸 OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm) - **100zł** <br>
🔋 WaveShare Li-polymer Battery HAT - **90zł** <br>
💾 microSD Card- **20zł** <br>
📦 Case - 3d printing cost approximately **100zł** <br>
**TOTAL** approximately **590 PLN** ~ **155 USD**


### 📋 Requirements
+ Raspberry Pi with **Raspberry Pi OS (Legacy) 64-bit, 11 (Bullseye), Kernel version: 6.1, Release date: October 22nd, 2024**.

+ **Python** version **3.9.2**.

### 🛠️ Raspberry Pi Configuration
1️⃣ Downloading files from the repository to Raspberry Pi  
2️⃣ Installing required libraries from the _**requirements.txt**_ file

You need to navigate to the directory with the downloaded files and enter the following command:
```console
veinfinder@veinfinder:~$ pip install -r requirements.txt
```

3️⃣ Creating a **Wifi Hotspot** + **DNS**
```console
veinfinder@veinfinder:~$ sudo apt update
veinfinder@veinfinder:~$ sudo apt install hostapd dnsmasq
```
![upadte](https://github.com/user-attachments/assets/b7a6e042-0657-4b7c-aadf-5bac396115c5)
```console
veinfinder@veinfinder:~$ sudo systemctl stop hostapd.service
veinfinder@veinfinder:~$ sudo systemctl stop dnsmasq.service
```
```console
veinfinder@veinfinder:~$ sudo nano /etc/dhcpcd.conf
```
![nanoDhcpcd](https://github.com/user-attachments/assets/d55f664e-44f7-48f4-9ddf-9a559562ac19)

At the end of the file, add:
```console
interface wlan0
static ip_address=192.168.1.254/24
nohook wpa_supplicant
```
![dhcpcfConf](https://github.com/user-attachments/assets/7ca19b8d-d14d-4894-adcd-490ff736356b)
```console
veinfinder@veinfinder:~$ sudo systemctl restart dhcpcd.service
```
```console
veinfinder@veinfinder:~$ sudo nano /etc/dnsmasq.conf
```
![nanoDns](https://github.com/user-attachments/assets/7b0149ea-94d1-4d69-879d-51a4b6f19b8e)

At the end of the file, add:
```console
interface=wlan0
dhcp-range=192.168.1.10,192.168.4.50,255.255.255.0,24h
address=/veinfinder/192.168.1.254
```
![dnsConf](https://github.com/user-attachments/assets/ba352c20-f706-4174-8923-d4e2cd386aae)

```console
veinfinder@veinfinder:~$ sudo systemctl restart dnsmasq.service
```
```console
veinfinder@veinfinder:~$ sudo nano /etc/hostapd/hostapd.conf
```
![hostapdConf](https://github.com/user-attachments/assets/b4956dc2-e1d8-4c37-99c3-a679078ff8ce)

Enter the following in the file:
```console
interface=wlan0
driver=nl80211
ssid=veinfinder
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=0
```
![hostapdConf2](https://github.com/user-attachments/assets/50bab076-257b-4539-889b-cf970107cbe2)

```console
veinfinder@veinfinder:~$ sudo nano /etc/default/hostapd
```
![nanoHostapd](https://github.com/user-attachments/assets/216693ec-5f70-4c62-b08e-558c90063556)
```console
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```
You need to find, uncomment **(remove the "#" character)**, and provide the path to the configuration file. It should look like this:  
![hostapdDeamon](https://github.com/user-attachments/assets/4119c998-4046-43ae-99f2-4af016eb99fc)

```console
veinfinder@veinfinder:~$ sudo systemctl unmask hostapd
veinfinder@veinfinder:~$ sudo systemctl enable hostapd
veinfinder@veinfinder:~$ sudo systemctl start hostapd.service
```
After running the command:
```console
veinfinder@veinfinder:~$ sudo systemctl status hostapd
```
A similar response should appear with the status **"active"**
![hostapdStatus2](https://github.com/user-attachments/assets/a3b2d7cb-4f9b-4fca-a00b-b7eeea2c8ef3)


4️⃣ Setting up automatic startup for _**app.py**_ at device boot
```console
veinfinder@veinfinder:~$ sudo nano /etc/rc.local
```
![rclocal1](https://github.com/user-attachments/assets/ba9a0143-62c0-44bf-9e0d-09af27a70fec)

It should be added at the end, but **before** "exit 0": 
```console
sudo python3 FILE_PATH/app.py &
```
In this case:
```console
sudo python3 /home/veinfinder/Desktop/Veinfinder/app.py &
```
![rclocal2](https://github.com/user-attachments/assets/f5397edf-acf6-47d1-87d5-9f204c1c0271)

5️⃣ For better performance, you can disable Bluetooth and enable console mode

*Disabling Bluetooth*
```console
sudo nano /boot/config.txt
```
![turnOffBluetooth](https://github.com/user-attachments/assets/45ce6797-daef-42af-b69f-b0f11628796f)

At the end of the file, add:
```console
dtoverlay=disable-bt
```
![turnOffBluetooth2](https://github.com/user-attachments/assets/2fb94867-1a41-4351-9a5b-497a54de86ae)

*Enabling Console Mode* 
```console
sudo raspi-config
```
![raspiconfig1](https://github.com/user-attachments/assets/a0e7d2a5-7848-4127-bcb4-2b11ba810962)

_*"System Options -> Boot / Auto Login Select boot... -> Console Autologin..."*_
![raspiconfig2](https://github.com/user-attachments/assets/4fd2fa95-dcb5-454a-a008-00765b29e31f)
![raspiconfig3](https://github.com/user-attachments/assets/e6f04bad-6b5e-4bc2-b5cc-6d20fed2e34d)
![raspiconfig4](https://github.com/user-attachments/assets/fbb8b272-0c7b-4fd4-95ad-99a471cfa3b2)

✅ **READY!**

### ▶️ Usage
To turn on the device, press the **ON/OFF** button. <br>
To turn off the device, press the **ON/OFF** button twice. <br>
The device can be charged using USB TYPE C (Fast charging supported).  _(The five LED indicators show the battery level and charging status)_
