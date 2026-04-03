import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomeComponent from "./components/HomeComponent";
import LoginComponent from "./components/LoginComponent";
import RestrauntComponent from "./components/RestrauntComponent";
import UserRegisteration from "./components/UserRegisterationComponent";
import AdminComponent from "./components/AdminComponent";
import UserDetailsComponent from "./components/UserDetailsComponent";
import UpdateUserProfileComponent from "./components/UpdateUserProfileComponent";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomeComponent />} />
                <Route path="/login" element={<LoginComponent />} />
                <Route path="/restraunt" element={<RestrauntComponent />} />
                <Route path="/register" element={<UserRegisteration />} />
                <Route path="/admin" element={<AdminComponent />} />
                <Route path="/userdetails" element={<UserDetailsComponent />} />
                <Route path="/update-profile" element={<UpdateUserProfileComponent />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App;