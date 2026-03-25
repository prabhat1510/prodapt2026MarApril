import './App.css'
import CustomerComponent from './components/CustomerComponent'
//Functional Component
function App() {
  // <> </> is called fragment
  return (
    <>
      <p className='c1'>Hello Mukesh</p>
      {/*<p>I am from Hyderabad</p>
      <p>I am working at Prodapt</p>*/}
      <p>I am a software engineer</p>
      <button className='btn btn-primary'>Click Me</button>
      <CustomerComponent />
    </>
  )
}c

export default App
