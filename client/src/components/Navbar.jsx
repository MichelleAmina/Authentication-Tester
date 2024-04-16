import { NavLink } from 'react-router-dom';


function Navbar(){
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <NavLink className="navbar-brand" href="#">
                <b>E-Website</b>
            </NavLink>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
              <ul className="navbar-nav ml-auto">
                <li className="nav-item active">
                  <NavLink className="nav-link" to='/'>HOME <span className="sr-only">(current)</span></NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to='/login'>LOGIN</NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to='/register'>REGISTER</NavLink>
                </li>
                
            
              </ul>
            </div>
        </nav>
        </div>
    )

}

export default Navbar 