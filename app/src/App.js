import React, { useState } from "react";

import "./App.css";

import Clientes from "./components/Clientes/Clientes";
import NuevoCliente from "./components/NuevoCliente/NuevoCliente";

import Peliculas from "./components/Peliculas/Peliculas";
import NuevoPelicula from "./components/NuevoPelicula/NuevoPelicula";

function App() {
  const [peliculas, setPeliculas] = useState([
    { inventario: 1, nombre: "Spiderman", genero: "Sam R.", duracion: 5 },
    { inventario: 2, nombre: "Batman", genero: "Tim Burton", duracion: 3 },
    { inventario: 3, nombre: "Inception", genero: "Christopher Nolan", duracion: 4 },
  ]);

  const [clientes, setClientes] = useState([
    {
      nombre: "Fernando",
      apellidoPaterno: "Fong",
      password: 313320679,
    },
    {
      nombre: "Valeria",
      apellidoPaterno: "Garcia",
      password: 314006088,
    },
    {
      nombre: "Erick",
      apellidoPaterno: "Martinez",
      password: 414890123,
    },
  ]);

  const agregarCliente = (cliente) => {
    const nuevoCliente = [cliente, ...clientes];
    setClientes(nuevoCliente);
    console.log(nuevoCliente);
  };

  const eliminarCliente = (index) => {
    const nuevaListaClientes = [...clientes];
    nuevaListaClientes.splice(index, 1);
    setClientes(nuevaListaClientes);
  };
  

  const agregarPelicula = (pelicula) => {
    const nuevoPelicula = [pelicula, ...peliculas];
    setPeliculas(nuevoPelicula);
    console.log(nuevoPelicula);
  };

  const eliminarPelicula = (index) => {
    const nuevaListaPeliculas = [...peliculas];
    nuevaListaPeliculas.splice(index, 1);
    setPeliculas(nuevaListaPeliculas);
  };

 

  return (
    <div className="App">
      <NuevoCliente onAgregarCliente={agregarCliente} />
      <Clientes clientes={clientes} onEliminarCliente={eliminarCliente} />

      <NuevoPelicula onAgregarPelicula={agregarPelicula} />
      <Peliculas peliculas={peliculas} onEliminarPelicula={eliminarPelicula} />
    </div>
  );
}

export default App;
