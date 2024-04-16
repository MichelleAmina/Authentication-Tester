import { NavLink, useNavigate} from "react-router-dom"
import { useState } from "react"

function Login(){

    const navigate = useNavigate();

    const [email, setEmail] = useState()
    const [password, setPassword] = useState()

    /*
    const setData = async(e) => {
        e.preventDefault()

        const res = await fetch('http://127.0.0.1:5555/adminLogin', {
            method: 'POST',
            headers : {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email, password
            })
        });
        const data = await res.json()
        //console.log(res)

        if (res.status === 201){
        
            localStorage.setItem('access_token', data.access_token)
            window.alert('Login successful')
            navigate('/')
        }
        else {
            window.alert('Login failed, Invalid credentials')
            
        }
    }
    */
    const setData = async (e) => {
        e.preventDefault();
    
        try {
            const res = await fetch('http://127.0.0.1:5555/adminLogin', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email,
                    password
                })
            });
    
            if (res.status === 201) {
                const data = await res.json();
                localStorage.setItem('access_token', data.access_token);
                window.alert('Login successful');
                navigate('/');
            } else {
                window.alert('Login failed, Invalid credentials');
            }
        } catch (error) {
            console.error('Error:', error);
            window.alert('An error occurred while processing your request');
        }
    };
    

    return (
        <>
        <section>
            <div className="container mt-5">
                <div className='row'>

                    <div className="col-sm-6 offset-md-3 offset-sm-1 ">
                        <form method="POST">

                            <div className="form-group">
                                <label htmlFor="email">Email</label>
                                <input type="email" className="form-control" id="email" name="email" placeholder="Enter your Email" value={email} onChange={(e) => setEmail(e.target.value)}/>
                            </div>

                            <div className="form-group">
                                <label htmlFor="password">Password</label>
                                <input type="password" className="form-control" id="password" name="password" placeholder="Enter your Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                            </div>

                            <NavLink to='/register'>No account? register here!</NavLink><br /><br />
                            <button type="submit" className="btn btn-primary" id='login' name='login' onClick={setData}>Login</button>

                        </form>
                    </div>

                </div>

            </div>
        </section>
    </>

    )

}

export default Login