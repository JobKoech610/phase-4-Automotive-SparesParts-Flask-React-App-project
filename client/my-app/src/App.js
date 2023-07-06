import './App.css';
import Header from './Header';
import { Routes, Route } from "react-router-dom"
import Navbar from './Navbar';

import AccessoryList from './AccessoryList'
import Accessory from './Accessory'
import Home from './Home'

function App() {
  return (
    <div className="App">
       <Header/>
       {/* <AccessoryList /> */}
      <Navbar/>
      <Routes>
      
        <Route exact path='/'element={<Home/>}/>
        <Route path='/accessory' element={<Accessory/>}/>
        <Route path='/accessorylist' element={<AccessoryList/>}/>
      
      </Routes> 
    </div>
  );
}

export default App;
