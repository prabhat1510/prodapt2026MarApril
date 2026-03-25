const LoginComponent = (props) => {
    //Destructuring
    const { username, password } = props.loginDetails;
    return (
        <div>
            <h1>Login</h1>
            {/* <p>{props.userDetails.username}</p>
            <p>{props.userDetails.password}</p> */}
            <p>{username}</p>
            <p>{password}</p>
        </div>
    )
}

export default LoginComponent