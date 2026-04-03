import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { loginUser } from "../services/user_service";

function Login() {
    const navigate = useNavigate();
    const [login, setLogin] = useState({
        username: "",
        password: ""
    });
    const [error, setError] = useState("");

    const handleOnChange = (e) => {
        setLogin({
            ...login,
            [e.target.name]: e.target.value
        })
    }
    const handleLogin = async (e) => {
        e.preventDefault();
        setError("");
        try {
            console.log("Attempting login with:", login);
            const data = await loginUser(login);
            console.log("Login success:", data);

            // Store common login response data
            localStorage.setItem("access_token", data.access_token);
            localStorage.setItem("refresh_token", data.refresh_token);
            localStorage.setItem("roles", JSON.stringify(data.roles));
            localStorage.setItem("token_type", data.token_type);

            alert("Login successful!");
            navigate("/userdetails");
        } catch (err) {
            console.error("Login Error:", err);
            setError("Invalid username or password. Please try again.");
        }
    }
    return (
        <div className="container">
            <div className="row">
                <h1>Login</h1>
                {error && <div className="alert alert-danger">{error}</div>}
                <Link to="/">Home</Link>
            </div>
            <div className="row">
                <div className="col-md-6">
                    <form onSubmit={handleLogin}>
                        <div className="mb-3">
                            <label htmlFor="username">Username</label>
                            <input type="text" className="form-control" id="username" name="username" value={login.username} placeholder="Username" onChange={handleOnChange} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="password">Password</label>
                            <input type="password" className="form-control" id="password" name="password" value={login.password} placeholder="Password" onChange={handleOnChange} />
                        </div>
                        <button type="submit" className="btn btn-primary">Login</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login