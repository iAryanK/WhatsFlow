# Packages
import Driver
from selenium import webdriver  # used to automatically open chrome browser using python
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains    # used to automatically press key on browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from tkinter import ttk
from customtkinter import CTk, StringVar, CTkFrame, CTkTextbox, CTkEntry, CTkButton, CTkLabel, CTkCheckBox, filedialog
import threading
import pyperclip as pc

# Create functions to handle the placeholder behavior
def handle_phone_numbers(event):
    if phone_numbers_text.get("1.0", "end-1c") == phone_numbers_text_placeholder:
        phone_numbers_text.delete("1.0", "end")
        if CTk._get_appearance_mode(root) == 'light':
            phone_numbers_text.configure(text_color="black")
        else:
            phone_numbers_text.configure(text_color="white")

def handle_message(event):
    if message_text.get("1.0", "end-1c") == message_text_placeholder:
        message_text.delete("1.0", "end")
        if CTk._get_appearance_mode(root) == 'light':
            message_text.configure(text_color="black")
        else:
            message_text.configure(text_color="white")
    
def handle_image(event):
    if image.get() == image_placeholder:
        image.delete("0", "end")
        if CTk._get_appearance_mode(root) == 'light':
            image.configure(text_color="black")
        else:
            image.configure(text_color="white")

def handle_doc(event):
    if document.get() == doc_placeholder:
        document.delete("0", "end")
        if CTk._get_appearance_mode(root) == 'light':
            document.configure(text_color="black")
        else:
            document.configure(text_color="white")

def handle_focus_out(event):
    if phone_numbers_text.get("1.0", "end-1c") == "":
        phone_numbers_text.insert("1.0", phone_numbers_text_placeholder)
        phone_numbers_text.configure(text_color="gray")
    
    elif message_text.get("1.0", "end-1c") == "":
        message_text.insert("1.0", message_text_placeholder)
        message_text.configure(text_color="gray")
    
    elif image.get() == "":
        image.insert("0", image_placeholder)
        image.configure(text_color="gray")

    elif document.get() == "":
        document.insert("0", doc_placeholder)
        document.configure(text_color="gray")

def selectImg():
    file = filedialog.askopenfile()
    if file is not None:
        image.delete("0", "end")
        image.insert("end",file.name)

def selectFile():
    file = filedialog.askopenfile()
    if file is not None:
        document.delete("0", "end")
        document.insert("end",file.name)

def deleteChat(driver, num):
    # ensure that the chat to be deleted contains the same number on the top bar that should be deleted. Also, self chat should never be deleted
    receiver_number = num[-10:]
    receiver = "+91 " + receiver_number[0:5] + " " + receiver_number[5:]
    
    verify_receiver = driver.find_element(By.CSS_SELECTOR, "._amig ._aou8 .x1iyjqo2")
    if ((verify_receiver.text != receiver) or (receiver_number == (self_number.get())[-10:])) :
        return

    # click on delete chat option
    driver.find_element(By.CSS_SELECTOR, "._amih ._ajv7").click()
    WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Delete chat']")))
    driver.find_element(By.CSS_SELECTOR, "div[aria-label='Delete chat']").click()

    # click on delete chat button
    WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Delete this chat?']")))
    WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, "//div[text()=\"Delete chat\"]")))
    delete_chat_button = driver.find_element(By.XPATH, "//div[text()=\"Delete chat\"]")
    if(delete_chat_button.text == "Delete chat"):
        delete_chat_button.click()
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//span[@data-icon=\"lock-small\"]")))
    else:
        driver.find_element(By.XPATH, "//div[text()=\"Cancel\"]").click()
    
def sendMessage():
    if (phone_numbers_text.get("0.0", "end-1c") == phone_numbers_text_placeholder or len(phone_numbers_text.get("0.0", "end-1c")) == 0):
        jobvar.set("Enter phone numbers of receivers.")
        return
    
    if (self_number.get() == "") :
        jobvar.set("Carefully enter your whatsapp number in the required field.")
        return
    
    s = 0
    f = 0
    successvar.set("Success  |  Failure")
    jobvar.set("Processing...")
    send_message_button.configure(state="disabled")

    with open("numbers.txt", 'w') as file:
        file.writelines(phone_numbers_text.get("0.0", "end-1c"))
    
    with open("message.txt", 'w') as file:
        file.writelines(message_text.get("0.0","end-1c"))
            
    # Message Text (not encoded)
    with open('message.txt', 'r') as file:
        msg = file.read()
        pc.copy(msg)

    try:
        Driver.install_driver()
        driver = webdriver.Chrome()
        link = 'https://web.whatsapp.com'
        driver.get(link)
        WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-icon=\"lock-small\"]")))
    except Exception as e:
        print("[EXCEPTION IN DRIVER INSTALL]", e)
        if (driver):
            driver.quit()
        jobvar.set("Something unusual occurred. Retry!")
        send_message_button.configure(state="normal")
        return

    time.sleep(action_time*3)
    
    WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-icon=\"lock-small\"]")))
    num = (self_number.get())[-10:]
    link = f'https://web.whatsapp.com/send/?phone=91{num}'
    driver.get(link)

    WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[title='Message yourself']")))

    time.sleep(action_time)

    with open('numbers.txt', 'r') as file:
        for n in file.readlines():
            try:
                # Enter number in personal chat
                num = n.rstrip()
                if (num == ""):
                    continue
                action_sendNumber = ActionChains(driver)
                action_sendNumber.send_keys(num).perform()
                WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label=\"Send\"]")))
                driver.find_element(By.XPATH, "//button[@aria-label=\"Send\"]").click()  # Raises exception if such link text not found.


                WebDriverWait(driver, 300).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, "span[aria-label=' Pending ']")))
                driver.find_element("link text", f"{num}").click()  # Raises exception if such link text not found.
                
                WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Copy phone number']")))
                driver.find_element(By.CSS_SELECTOR, "div[aria-label='Chat with ']").click()

                # Wait for new chat page to load 
                if (num[-10:] != (self_number.get())[-10:]) :
                    WebDriverWait(driver, 300).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Message yourself']")))

                # Wait for type message box to appear before start typing the message 
                WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Type a message']")))

                # Click on button to load the input DOM
                if doc_path.get() != doc_placeholder and len(doc_path.get()) != 0 :
                    attach_btn = driver.find_element(By.CSS_SELECTOR, "span[data-icon='plus']")
                    attach_btn.click()
                    time.sleep(action_time)
                    # Find and send doc path to input
                    file_input = driver.find_element(By.CSS_SELECTOR, "input[accept='*']")
                    file_path = doc_path.get().strip("\"")
                    file_input.send_keys(file_path)
                    time.sleep(action_time)
                    # Start the action chain to write the message
                    action_sendDoc = ActionChains(driver)

                    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//span[@data-icon=\"send\"]")))
                    driver.find_element(By.XPATH, "//span[@data-icon=\"send\"]").click()

                # Click on button to load the input DOM
                if image_path.get() != image_placeholder and len(image_path.get()) !=0 :
                    attach_btn = driver.find_element(By.CSS_SELECTOR, "span[data-icon='plus']")
                    attach_btn.click()
                    time.sleep(action_time)
                    # Find and send image path to input
                    msg_input = driver.find_element(By.CSS_SELECTOR, "input[accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                    img_path = image_path.get().strip("\"")
                    msg_input.send_keys(img_path)
                    
                    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='emoji-input']")))                    
                else:
                    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='smiley']")))

                pc.copy(msg)
                action_sendMessage = ActionChains(driver)
                time.sleep(action_time)

                if image_path.get() == image_placeholder and len(image_path.get()) ==0 :
                    driver.find_element(By.XPATH, f"//div[@aria-label=\"Type a message\"]").click()

                action_sendMessage.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

                if image_path.get() == image_placeholder and len(image_path.get()) ==0 :
                    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label=\"Send\"]")))
                    driver.find_element(By.XPATH, "//button[@aria-label=\"Send\"]").click()
                else:
                    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//span[@data-icon=\"send\"]")))
                    driver.find_element(By.XPATH, "//span[@data-icon=\"send\"]").click()
                
                time.sleep(action_time/2)
                WebDriverWait(driver, 300).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, "span[aria-label=' Pending ']")))
                
                s = s+1
                successvar.set(f"Success: {s}  |  Failure: {f}")
                success_status.update()
                
                # if checkbox is checked
                if (deleteChat_checkbox.get()):
                    deleteChat(driver, num)

            except Exception as e:
                print("[EXCEPTION] ", e)
                jobvar.set(f"An error occured for {n.strip()}")
                f = f+1
                successvar.set(f"Success: {s}  |  Failure: {f}")

            finally:
                try:
                    driver.find_element(By.XPATH, "//span[text()=\"(You)\"]").click()
                    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='Message yourself']")))
                except Exception as e:
                    print("[EXCEPTION IN FINALLY BLOCK] ", e)
                    jobvar.set("Ready")
                    driver.quit()
                    send_message_button.configure(state="normal")
                    return

    # Quit the driver
    driver.quit()
    jobvar.set("Ready")
    send_message_button.configure(state="normal")

def connectMe():
    threading.Thread(target=sendMessage).start()

root = CTk()
root.title('WhatsFlow 6.6.1')
root.geometry('800x450')
root.iconbitmap('flowicon.ico')
root.minsize(650,370)

image_path = StringVar()
doc_path = StringVar()
jobvar = StringVar()
successvar = StringVar()
failurevar = StringVar()

action_time = 1                 # Set time for button click action

mainframe = CTkFrame(root, corner_radius=0)
mainframe.pack(fill='both', expand='true')
left_frame = CTkFrame(mainframe)
right_frame = CTkFrame(mainframe)
image_frame = CTkFrame(right_frame, corner_radius=0)
file_frame = CTkFrame(right_frame, corner_radius=0)
self_number_frame = CTkFrame(left_frame, corner_radius=0)

self_number = CTkEntry(self_number_frame, height=35, placeholder_text="Carefully enter your whatsapp number here.")
self_number.pack(expand='true', fill='x', pady=(5, 5))

phone_numbers_text = CTkTextbox(left_frame, width=300, corner_radius=0, wrap='word')
phone_numbers_text.pack(side='top', expand='true', fill='both')

deleteChat_checkbox = CTkCheckBox(left_frame, text=" Want to delete chat after sending message?", border_width=1.5, font=('CTkDefaultFont', 13.5))
deleteChat_checkbox.pack(side='bottom', pady=(5,5))

message_text = CTkTextbox(right_frame, corner_radius=0, wrap='word')
message_text.pack(expand='true', fill='both', pady=(0, 10))

image = CTkEntry(image_frame, height=35, textvariable=image_path)
image.pack(side='left',expand='true', fill='x', padx=(0, 10))

select_img_button = CTkButton(image_frame, text='Image/Video', font=('CTkDefaultFont', 20), command=selectImg)
select_img_button.pack(side='right')
image_frame.pack(fill='x')

document = CTkEntry(file_frame, height=35, textvariable=doc_path)
document.pack(side='left',expand='true', fill='x', padx=(0, 10))

select_doc_button = CTkButton(file_frame, text='Document', font=('CTkDefaultFont', 20), command=selectFile)
select_doc_button.pack(side='right')
file_frame.pack(fill='x', pady=(5, 0))

send_message_button = CTkButton(right_frame, text='START SENDING MESSAGES', width=90, font=('CTkDefaultFont', 20), corner_radius=5, command=connectMe)
send_message_button.pack(side='bottom', fill='x', pady=(10, 0))

left_frame.pack(side='left', fill='y', padx='10', pady='10')
self_number_frame.pack(side='top', fill='both')
right_frame.pack(side='right', fill='both', expand='true', padx='10', pady='10')

sbar = CTkFrame(root, height=25, corner_radius=0)
sbar.pack(side="bottom", fill="x",  pady=(2, 0))

job_status = CTkLabel(sbar, textvariable=jobvar)
job_status.pack(padx=10, anchor='w', side='left')
jobvar.set("Ready")

success_status = CTkLabel(sbar, textvariable=successvar)
success_status.pack(padx=10, anchor='e', side='right')
successvar.set("Success  |  Failure")

# Define a placeholder text
phone_numbers_text_placeholder = "Enter phone numbers here. Only one phone number should be entered in each line."
message_text_placeholder = "Enter the message here, that you want to send."
image_placeholder = "Absolute path of the image/video, if any."
doc_placeholder = "Absolute path of document, if any."

# Set the initial placeholder text
phone_numbers_text.insert("1.0", phone_numbers_text_placeholder)
phone_numbers_text.configure(text_color='gray')
message_text.insert("1.0", message_text_placeholder)
message_text.configure(text_color='gray')
image.insert("0", image_placeholder)
image.configure(text_color='gray')
document.insert("0", doc_placeholder)
document.configure(text_color='gray')

# Bind the events to the widget
phone_numbers_text.bind("<FocusIn>", handle_phone_numbers)
phone_numbers_text.bind("<FocusOut>", handle_focus_out)
message_text.bind("<FocusIn>", handle_message)
message_text.bind("<FocusOut>", handle_focus_out)
image.bind("<FocusIn>", handle_image)
image.bind("<FocusOut>", handle_focus_out)
document.bind("<FocusIn>", handle_doc)
document.bind("<FocusOut>", handle_focus_out)

root.mainloop()