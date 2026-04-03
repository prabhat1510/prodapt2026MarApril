import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { getUserProfile } from "../services/user_service";

function UserDetailsComponent() {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const fetchUserData = async () => {
            setLoading(true);
            setError("");
            try {
                const data = await getUserProfile();
                console.log("Fetched User Profile:", data);
                setUser(data);
                setLoading(false);
            } catch (err) {
                console.error("Error fetching profile:", err);
                setError("Failed to load user information. Please log in again.");
                setLoading(false);
                // Optional: redirect to login if unauthorized
                // if (err.response && err.response.status === 401) navigate("/login");
            }
        };

        const token = localStorage.getItem("access_token");
        if (!token) {
            setError("No active session. Please log in.");
            setLoading(false);
            navigate("/login");
        } else {
            fetchUserData();
        }
    }, [navigate]);

    if (loading) return <div className="container mt-5"><h3>Loading user profile...</h3></div>;

    if (error) return (
        <div className="container mt-5">
            <div className="alert alert-danger">{error}</div>
            <Link to="/login" className="btn btn-primary">Go to Login</Link>
        </div>
    );

    return (
        <div className="container mt-5">
            <div className="card shadow">
                <div className="card-header bg-primary text-white">
                    <h2 className="mb-0">User Profile Details</h2>
                </div>
                <div className="card-body">
                    {user && (
                        <div className="user-info">
                            <div className="row mb-3">
                                <div className="col-md-3 font-weight-bold">Username:</div>
                                <div className="col-md-9">{user.username}</div>
                            </div>
                            <div className="row mb-3">
                                <div className="col-md-3 font-weight-bold">Email:</div>
                                <div className="col-md-9">{user.email}</div>
                            </div>
                            <div className="row mb-3">
                                <div className="col-md-3 font-weight-bold">First Name:</div>
                                <div className="col-md-9">{user.firstName || "N/A"}</div>
                            </div>
                            <div className="row mb-3">
                                <div className="col-md-3 font-weight-bold">Last Name:</div>
                                <div className="col-md-9">{user.lastName || "N/A"}</div>
                            </div>
                            <div className="row mb-3">
                                <div className="col-md-3 font-weight-bold">Phone:</div>
                                <div className="col-md-9">{user.phone || "N/A"}</div>
                            </div>
                            <div className="row mb-3">
                                <div className="col-md-3 font-weight-bold">Roles:</div>
                                <div className="col-md-9">
                                    {user.roles && user.roles.map((role, index) => (
                                        <span key={index} className="badge badge-info bg-secondary mr-2">{role}</span>
                                    ))}
                                </div>
                            </div>
                            <hr />
                            <h5>Home Address</h5>
                            {user.homeAddress ? (
                                <p>{user.homeAddress.street}, {user.homeAddress.city}, {user.homeAddress.state} {user.homeAddress.zip}</p>
                            ) : <p>No home address specified.</p>}

                            {user.restaurant_ids && user.restaurant_ids.length > 0 && (
                                <>
                                    <hr />
                                    <h5>Owned Restaurants</h5>
                                    <ul>
                                        {user.restaurant_ids.map((id, index) => (
                                            <li key={index}>Restaurant ID: {id}</li>
                                        ))}
                                    </ul>
                                </>
                            )}
                        </div>
                    )}
                </div>
                <div className="card-footer d-flex justify-content-between">
                    <Link to="/" className="btn btn-secondary">Home</Link>
                    <button className="btn btn-warning" onClick={() => navigate("/update-profile", { state: { user } })}>Edit Profile</button>
                    <button className="btn btn-danger" onClick={() => { localStorage.clear(); navigate("/login"); }}>Logout</button>
                </div>
            </div>
        </div>
    );
}

export default UserDetailsComponent;