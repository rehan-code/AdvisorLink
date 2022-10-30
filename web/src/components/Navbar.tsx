import Logo from '../static/logo_img.png';

const Navbar = () => {
    return (
        <div className="w-screen flex justify-center items-center p-2 z-10" id='Navbar'>
            <div className="w-screen flex bg-white justify-between">
                <a href='/'>
                    <div className="flex justify-center items-center gap-2 pl-3">
                        <img src={Logo} alt="advisorlink logo"/>
                        <div className="text-4xl"><strong>Advisor</strong>Link</div>
                    </div>
                </a>
                <div className="flex justify-center items-center gap-8 text-2xl pr-10">
                    <div><a href='/'>Calendar</a></div>
                    <div><a href='/'>About Us</a></div>
                    <div><a href='/'>Contact</a></div>
                </div>
            </div>
        </div>
    )
}

export default Navbar;