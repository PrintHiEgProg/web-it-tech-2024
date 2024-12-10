import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Header from "./components/header/header";
import FloatButton from "./components/float-button/float-button";
import MainContent from "./components/main-content/main-content";
import Projects from "./components/projects/projects";
import Registration from './components/registration/registration'
import Login from "./components/login/login";
import NotFound from "./components/not-found/not-found";
import Vacancy from "./components/vacancy/vacancy";

function App() {

  const userLogIn = false;

  return (
    <>
     <Router>
      <Header isLogedIn={userLogIn} />
      <Routes>
        <Route path="*" element={<MainContent><NotFound/></MainContent>}/>
        <Route path="/projects" element={<MainContent><Projects/></MainContent>} />
        <Route path="/registration" element={<MainContent><Registration/></MainContent>} />
        <Route path="/login" element={<MainContent><Login/></MainContent>} />
        <Route path="/vacancy" element={<MainContent><Vacancy/></MainContent>} />
      </Routes>
      <FloatButton />
     </Router>
    </>
  );
}

export default App;