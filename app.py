import streamlit as st
import time
from datetime import datetime

st.title("Ando con sueño amor")
st.write("Vamonos a dormir amor")
# Mostrar la hora actual con Python
placeholder = st.empty()  # Espacio reservado para la hora


# Agregar un GIF
st.markdown("![Alt Text](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGszYjFoc2kxYmdtb3QyaXI5Y2x6eWlmZHh6djExNjU3NmpxM2RqNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uk4Va5MkRp2bfkOk6f/giphy.gif)")

current_time = datetime.now().strftime("%I:%M:%S %p")
placeholder.write(f"### Que ya son las {current_time}")