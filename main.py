import customtkinter
import requests
from PIL import Image,ImageTk
import pywinstyles,pywinstyles
import pandas as pd
from historydata import*
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# STEP 1 - Making window
window= customtkinter.CTk(fg_color="#022045")
window.geometry("400x580")
window.resizable(False,False)
window.title("Baldova pračka peněz")
window.iconbitmap("images/cryptocurrency.ico")


# STEP 2 - SETTINGS
Helvetica_15 = customtkinter.CTkFont(family="Helvetica",size=15,weight="bold")
Helvetica_30 = customtkinter.CTkFont(family="Helvetica",size=30,weight="bold")
Helvetica_15 = customtkinter.CTkFont(family="Helvetica",size=15,weight="bold")
crypto_data = {'Name': [], 'Price': []}
# STEP 3 - API Scrapping
url = "https://api.coincap.io/v2/assets"

r = (requests.get(url)).json()
bitcoin = round(float(r["data"][0]["priceUsd"]),2)
ethereum = round(float(r["data"][1]["priceUsd"]),2)
solana = round(float(r["data"][4]["priceUsd"]),4)
xrp = round(float(r["data"][6]["priceUsd"]),4)
binance = round(float(r["data"][3]["priceUsd"]),2)

def update_data():
  # Update data logic (API call, data processing)
    global bitcoin, ethereum, tether, xrp, binance
    r = (requests.get(url)).json()
    bitcoin = round(float(r["data"][0]["priceUsd"]),1)
    ethereum = round(float(r["data"][1]["priceUsd"]),2)
    solana = round(float(r["data"][4]["priceUsd"]),2)
    xrp = round(float(r["data"][6]["priceUsd"]),2)
    binance = round(float(r["data"][3]["priceUsd"]),2)

  # Update labels with new data
    bitcoin_price.configure(text=f"{bitcoin}$")
    ethereum_price.configure(text=f"{ethereum}$")
    xrp_price.configure(text=f"{xrp}$")
    binance_price.configure(text=f"{binance}$")
    solana_price.configure(text=f"{solana}$")

  # Schedule next update after 2 seconds
    window.after(2000, update_data)

# STEP 4 - Button, Labels, Images
# - RECTANGLES
first_rectangle = customtkinter.CTkLabel(window, width=350,height=80,fg_color="#023469",text="",corner_radius=10,bg_color="#00244d")
pywinstyles.set_opacity(first_rectangle,color="#00244d",value=1)
first_rectangle.place(x=25,y= 50)

second_rectangle = customtkinter.CTkLabel(window, width=350,height=80,fg_color="#023469",text="",corner_radius=10,bg_color="#00244d")
pywinstyles.set_opacity(first_rectangle,color="#00244d",value=1)
second_rectangle.place(x=25,y= 150)

third_rectangle = customtkinter.CTkLabel(window, width=350,height=80,fg_color="#023469",text="",corner_radius=10,bg_color="#00244d")
pywinstyles.set_opacity(first_rectangle,color="#00244d",value=1)
third_rectangle.place(x=25,y= 250)

forth_rectangle = customtkinter.CTkLabel(window, width=350,height=80,fg_color="#023469",text="",corner_radius=10,bg_color="#00244d")
pywinstyles.set_opacity(first_rectangle,color="#00244d",value=1)
forth_rectangle.place(x=25,y= 350)

finth_rectangle = customtkinter.CTkLabel(window, width=350,height=80,fg_color="#023469",text="",corner_radius=10,bg_color="#00244d")
pywinstyles.set_opacity(first_rectangle,color="#00244d",value=1)
finth_rectangle.place(x=25,y= 450)

# - INFO INSIDE OF RECTANGLES
#   BITCOIN
bitcoin_text = customtkinter.CTkLabel(first_rectangle, text="BITCOIN",font=Helvetica_15)
bitcoin_text.place(x=35,y=5)

bitcoin_image = customtkinter.CTkImage(Image.open("images/bitcoin.png"),size=(15,15))
bitcoin_label = customtkinter.CTkLabel(first_rectangle,image=bitcoin_image,text="")
bitcoin_label.place(x=10,y=5)

bitcoin_price = customtkinter.CTkLabel(first_rectangle,font=Helvetica_30,text=f"{bitcoin}$")
bitcoin_price.place(x=30,y=35)

#   ETHEREUM
ethereum_text = customtkinter.CTkLabel(second_rectangle, text="ETHEREUM",font=Helvetica_15)
ethereum_text.place(x=35,y=5)

ethereum_image = customtkinter.CTkImage(Image.open("images/ethereum.png"),size=(15,15))
ethereum_label = customtkinter.CTkLabel(second_rectangle,image=ethereum_image,text="")
ethereum_label.place(x=10,y=5)

ethereum_price = customtkinter.CTkLabel(second_rectangle,font=Helvetica_30,text=f"{ethereum}$")
ethereum_price.place(x=30,y=35)

#   TETHER
solana_text = customtkinter.CTkLabel(third_rectangle, text="SOLANA",font=Helvetica_15)
solana_text.place(x=35,y=5)

solana_image = customtkinter.CTkImage(Image.open("images/solana.png"),size=(15,15))
solana_label = customtkinter.CTkLabel(third_rectangle,image=solana_image,text="")
solana_label.place(x=10,y=5)

solana_price = customtkinter.CTkLabel(third_rectangle,font=Helvetica_30,text=f"{solana}$")
solana_price.place(x=30,y=35)

#   XRP
xrp_text = customtkinter.CTkLabel(forth_rectangle, text="XRP",font=Helvetica_15)
xrp_text.place(x=35,y=5)

xrp_image = customtkinter.CTkImage(Image.open("images/xrp.png"),size=(15,15))
xrp_label = customtkinter.CTkLabel(forth_rectangle,image=xrp_image,text="")
xrp_label.place(x=10,y=5)

xrp_price = customtkinter.CTkLabel(forth_rectangle,font=Helvetica_30,text=f"{xrp}$")
xrp_price.place(x=30,y=35)

#   BINANCE
binance_text = customtkinter.CTkLabel(finth_rectangle, text="BINANCE",font=Helvetica_15)
binance_text.place(x=35,y=5)

binance_image = customtkinter.CTkImage(Image.open("images/binance.png"),size=(15,15))
binance_label = customtkinter.CTkLabel(finth_rectangle,image=binance_image,text="")
binance_label.place(x=10,y=5)

binance_price = customtkinter.CTkLabel(finth_rectangle,font=Helvetica_30,text=f"{binance}$")
binance_price.place(x=30,y=35)

# GRAPHS
# - BITCOIN
bitcoin_data = pd.DataFrame(bitcoin_prices)
bitcoin_data["date"] = pd.to_datetime(bitcoin_data["date"])

fig_1 = Figure(figsize=(2.3, 1.2), facecolor="#023469")
ax_1 = fig_1.add_subplot()
ax_1.set_facecolor("#023469")
ax_1.fill_between(x=bitcoin_data["date"], y1=bitcoin_data["amount"], alpha=0.3,color = "green")
ax_1.tick_params(labelsize=7, colors="green")
fig_1.autofmt_xdate()
ax_1.plot(bitcoin_data["date"], bitcoin_data["amount"], color="green")

ax_1.get_xaxis().set_visible(False)
ax_1.get_yaxis().set_visible(False)

ax_1.spines['top'].set_color('#023469')
ax_1.spines['bottom'].set_color('#023469')
ax_1.spines['left'].set_color('#023469')
ax_1.spines['right'].set_color('#023469')

canvas_btc = FigureCanvasTkAgg(figure=fig_1, master=first_rectangle)
canvas_btc.draw() 
canvas_btc.get_tk_widget().place(x=200, y=0)

# ETHEREUM
ethereum_data = pd.DataFrame(ethereum_prices)
ethereum_data["date"] = pd.to_datetime(ethereum_data["date"])

fig_2 = Figure(figsize=(2.3, 1.2), facecolor="#023469")
ax_2 = fig_2.add_subplot()
ax_2.set_facecolor("#023469")
ax_2.fill_between(x=ethereum_data["date"], y1=ethereum_data["amount"], alpha=0.3,color = "green")
ax_2.tick_params(labelsize=7, colors="green")
fig_2.autofmt_xdate()
ax_2.plot(ethereum_data["date"], ethereum_data["amount"], color="green")

ax_2.get_xaxis().set_visible(False)
ax_2.get_yaxis().set_visible(False)

ax_2.spines['top'].set_color('#023469')
ax_2.spines['bottom'].set_color('#023469')
ax_2.spines['left'].set_color('#023469')
ax_2.spines['right'].set_color('#023469')

canvas_eth = FigureCanvasTkAgg(figure=fig_2, master=second_rectangle)
canvas_eth.draw() 
canvas_eth.get_tk_widget().place(x=200, y=0)

# SOlana
sol_data = pd.DataFrame(solano_prices)
sol_data["date"] = pd.to_datetime(sol_data["date"])

fig_3 = Figure(figsize=(2.3, 1.2), facecolor="#023469")
ax_3 = fig_3.add_subplot()
ax_3.set_facecolor("#023469")
ax_3.fill_between(x=sol_data["date"], y1=sol_data["amount"], alpha=0.3,color = "green")
ax_3.tick_params(labelsize=7, colors="green")
fig_3.autofmt_xdate()
ax_3.plot(sol_data["date"], sol_data["amount"], color="green")

ax_3.get_xaxis().set_visible(False)
ax_3.get_yaxis().set_visible(False)

ax_3.spines['top'].set_color('#023469')
ax_3.spines['bottom'].set_color('#023469')
ax_3.spines['left'].set_color('#023469')
ax_3.spines['right'].set_color('#023469')

canvas_TET = FigureCanvasTkAgg(figure=fig_3, master=third_rectangle)
canvas_TET.draw() 
canvas_TET.get_tk_widget().place(x=200, y=0)

# XRP
xrp_data = pd.DataFrame(xrp_prices)
xrp_data["date"] = pd.to_datetime(xrp_data["date"])

fig_4 = Figure(figsize=(2.3, 1.2), facecolor="#023469")
ax_4 = fig_4.add_subplot()
ax_4.set_facecolor("#023469")
ax_4.fill_between(x=xrp_data["date"], y1=xrp_data["amount"], alpha=0.3,color = "green")
ax_4.tick_params(labelsize=7, colors="green")
fig_4.autofmt_xdate()
ax_4.plot(xrp_data["date"], xrp_data["amount"], color="green")

ax_4.get_xaxis().set_visible(False)
ax_4.get_yaxis().set_visible(False)

ax_4.spines['top'].set_color('#023469')
ax_4.spines['bottom'].set_color('#023469')
ax_4.spines['left'].set_color('#023469')
ax_4.spines['right'].set_color('#023469')

canvas_xrp = FigureCanvasTkAgg(figure=fig_4, master=forth_rectangle)
canvas_xrp.draw() 
canvas_xrp.get_tk_widget().place(x=200, y=0)

# BINACE COIN
bnb_data = pd.DataFrame(bnb_prices)
bnb_prices["date"] = pd.to_datetime(bnb_data["date"])

fig_5 = Figure(figsize=(2.3, 1.2), facecolor="#023469")
ax_5 = fig_5.add_subplot()
ax_5.set_facecolor("#023469")
ax_5.fill_between(x=bnb_data["date"], y1=bnb_data["amount"], alpha=0.3,color = "green")
ax_5.tick_params(labelsize=7, colors="green")
fig_5.autofmt_xdate()
ax_5.plot(bnb_data["date"], bnb_data["amount"], color="green")

ax_5.get_xaxis().set_visible(False)
ax_5.get_yaxis().set_visible(False)

ax_5.spines['top'].set_color('#023469')
ax_5.spines['bottom'].set_color('#023469')
ax_5.spines['left'].set_color('#023469')
ax_5.spines['right'].set_color('#023469')

canvas_xrp = FigureCanvasTkAgg(figure=fig_5, master=finth_rectangle)
canvas_xrp.draw() 
canvas_xrp.get_tk_widget().place(x=200, y=0)

# Initial data fetch
update_data()

# Inicialise app
window.mainloop()
