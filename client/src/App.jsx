import { useState } from 'react'
import { Route, Routes } from "react-router-dom";
import './App.css'
import Home from './components/Home'
import Login from './components/Login'
import Register from './components/Register'
import Navbar from './components/Navbar'

function App() {

  return (
    <div>
      <Navbar/>
      <Routes>
        <Route path='/' element={<Home/>}>Home</Route>
        <Route path='/login' element={<Login/>}>Home</Route>
        <Route path='/register' element={<Register/>}>Home</Route>
      </Routes>
    </div>
  )
}

export default App
