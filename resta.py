{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7e49bdbf-6c7b-4f2f-bffd-0f37e947f645",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import messagebox\n",
    "\n",
    "# Función para realizar la resta\n",
    "def restar():\n",
    "    try:\n",
    "        num1 = float(entry1.get())\n",
    "        num2 = float(entry2.get())\n",
    "        resultado = num1 - num2\n",
    "        label_resultado.config(text=f\"Resultado: {resultado}\")\n",
    "    except ValueError:\n",
    "        messagebox.showerror(\"Error\", \"Por favor ingresa números válidos\")\n",
    "\n",
    "# Crear ventana principal\n",
    "ventana = tk.Tk()\n",
    "ventana.title(\"Calculadora de Resta\")\n",
    "ventana.geometry(\"300x200\")\n",
    "ventana.resizable(False, False)\n",
    "\n",
    "# Etiquetas y campos de entrada\n",
    "tk.Label(ventana, text=\"Número 1:\").pack(pady=5)\n",
    "entry1 = tk.Entry(ventana)\n",
    "entry1.pack()\n",
    "\n",
    "tk.Label(ventana, text=\"Número 2:\").pack(pady=5)\n",
    "entry2 = tk.Entry(ventana)\n",
    "entry2.pack()\n",
    "\n",
    "# Botón para calcular la resta\n",
    "btn_restar = tk.Button(ventana, text=\"Restar\", command=restar)\n",
    "btn_restar.pack(pady=10)\n",
    "\n",
    "# Etiqueta para mostrar el resultado\n",
    "label_resultado = tk.Label(ventana, text=\"Resultado: \")\n",
    "label_resultado.pack(pady=5)\n",
    "\n",
    "# Ejecutar la ventana\n",
    "ventana.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04c67b3f-fa22-404e-baa9-8800f782875e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5876b00-e83a-4ae6-b595-9264b737a120",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
