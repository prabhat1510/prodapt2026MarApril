import "./Hello.css";
import { useState } from "react";

function Counter() {
    //count is a state variable, setCount is a function to update the state variable
    const [count, setCount] = useState(0);//useState is a hook function to initialize the state variable
    const increment = () => {
        setCount(count + 1);
    }
    const decrement = () => {
        setCount(count - 1);
    }
    return (
        <div className="hello-world">
            <h1>Counter</h1>
            <p>Count: {count}</p>
            {/*<button className="btn btn-primary" onClick={() => setCount(count + 1)}>Increment</button>
            <button className="btn btn-danger" onClick={() => setCount(count - 1)}>Decrement</button>*/}
            <button className="btn btn-primary" onClick={increment}>Increment</button>
            <button className="btn btn-danger" onClick={decrement}>Decrement</button>
        </div>
    )
}

export default Counter;