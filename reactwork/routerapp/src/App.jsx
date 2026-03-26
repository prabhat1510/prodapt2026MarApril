import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import TVKComponent from "./components/TVKComponent";
import TMCComponent from "./components/TMCComponent";
import BJPComponent from "./components/BJPComponent";
import DMKComponent from "./components/DMKComponent";
import CongressComponent from "./components/CongressComponent";
import HomeComponent from "./components/HomeComponent";

function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <h1 className="text-center my-4">Political Party Components</h1>

        <Routes>
          <Route path="/" element={<HomeComponent />} />
          <Route path="/bjp" element={<BJPComponent />} />
          <Route path="/dmk" element={<DMKComponent />} />
          <Route path="/tmc" element={<TMCComponent />} />
          <Route path="/congress" element={<CongressComponent />} />
          <Route path="/tvk" element={<TVKComponent />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App