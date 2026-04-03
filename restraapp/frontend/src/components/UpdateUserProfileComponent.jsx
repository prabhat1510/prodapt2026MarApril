import { useState, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { updateUserDetails } from "../services/user_service";

function UpdateUserProfileComponent() {
    const location = useLocation();
    const navigate = useNavigate();
    const passedUser = location.state?.user;

    const [user, setUser] = useState({
        id: "",
        username: "",
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        phone: "",
        homeAddress: { street: "", city: "", state: "", zip: "" },
        roles: []
    });

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    useEffect(() => {
        if (passedUser) {
            setUser({
                ...passedUser,
                password: passedUser.password || "" // Maintain password if needed or handle separately
            });
        } else {
            // If no user was passed, maybe redirect or fetch (but we'll assume it's passed)
            setError("No user data found to update.");
        }
    }, [passedUser]);

    const handleOnChange = (e) => {
        const { name, value } = e.target;
        if (name.startsWith("homeAddress.")) {
            const field = name.split(".")[1];
            setUser({
                ...user,
                homeAddress: { ...user.homeAddress, [field]: value }
            });
        } else {
            setUser({ ...user, [name]: value });
        }
    };

    const handleUpdate = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError("");
        try {
            console.log("Updating user:", user);
            await updateUserDetails(user);
            alert("Profile updated successfully!");
            navigate("/userdetails");
        } catch (err) {
            console.error("Update Error:", err);
            setError("Failed to update profile. Please try again.");
            setLoading(false);
        }
    };

    if (error && !passedUser) return (
        <div className="container mt-5">
            <div className="alert alert-danger">{error}</div>
            <Link to="/userdetails" className="btn btn-primary">Back to Profile</Link>
        </div>
    );

    return (
        <div className="container mt-5">
            <div className="card shadow">
                <div className="card-header bg-warning text-dark">
                    <h2 className="mb-0">Update User Profile</h2>
                </div>
                <div className="card-body">
                    <form onSubmit={handleUpdate}>
                        <div className="row">
                            <div className="col-md-6 mb-3">
                                <label className="form-label">First Name</label>
                                <input type="text" name="firstName" className="form-control" value={user.firstName} onChange={handleOnChange} />
                            </div>
                            <div className="col-md-6 mb-3">
                                <label className="form-label">Last Name</label>
                                <input type="text" name="lastName" className="form-control" value={user.lastName} onChange={handleOnChange} />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-6 mb-3">
                                <label className="form-label">Email</label>
                                <input type="email" name="email" className="form-control" value={user.email} onChange={handleOnChange} disabled />
                            </div>
                            <div className="col-md-6 mb-3">
                                <label className="form-label">Phone</label>
                                <input type="text" name="phone" className="form-control" value={user.phone} onChange={handleOnChange} />
                            </div>
                        </div>

                        <h4 className="mt-4">Home Address</h4>
                        <div className="row">
                            <div className="col-md-6 mb-3">
                                <label className="form-label">Street</label>
                                <input type="text" name="homeAddress.street" className="form-control" value={user.homeAddress.street} onChange={handleOnChange} />
                            </div>
                            <div className="col-md-6 mb-3">
                                <label className="form-label">City</label>
                                <input type="text" name="homeAddress.city" className="form-control" value={user.homeAddress.city} onChange={handleOnChange} />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-6 mb-3">
                                <label className="form-label">State</label>
                                <input type="text" name="homeAddress.state" className="form-control" value={user.homeAddress.state} onChange={handleOnChange} />
                            </div>
                            <div className="col-md-6 mb-3">
                                <label className="form-label">Zip Code</label>
                                <input type="text" name="homeAddress.zip" className="form-control" value={user.homeAddress.zip} onChange={handleOnChange} />
                            </div>
                        </div>

                        <div className="d-flex justify-content-between mt-4">
                            <Link to="/userdetails" className="btn btn-secondary">Cancel</Link>
                            <button type="submit" className="btn btn-success" disabled={loading}>
                                {loading ? "Updating..." : "Save Changes"}
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default UpdateUserProfileComponent;