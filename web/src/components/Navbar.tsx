import { Link } from 'react-router-dom';
import Logo from '../static/logo_img.png';

function Navbar() {
  return (
    <div className="w-screen flex justify-center items-center p-2 z-10" id="Navbar">
      <div className="w-screen flex bg-white justify-between">
        <Link to="/">
          <div className="flex justify-center items-center gap-2 pl-3">
            <img src={Logo} alt="advisorlink logo" />
            <div className="text-4xl">
              <strong>Advisor</strong>
              Link
            </div>
          </div>
        </Link>
        <div className="flex justify-center items-center gap-8 text-2xl pr-10">
          <div><Link to="/calendar">Calendar</Link></div>
          <div><Link to="/about">About Us</Link></div>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
