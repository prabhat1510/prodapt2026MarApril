import { Link } from "react-router-dom";

function HomeComponent() {
    return (
        <div className="container">
            <h1>Home</h1>
            <Link to="/login">Login</Link> |
            <Link to="/restraunt">Restraunt</Link> |
            <Link to="/register">User Registeration</Link> |
            <Link to="/restraunt">Restraunt Registeration</Link> |
            <Link to="/admin">Admin</Link>
        </div>
    )
}

export default HomeComponent