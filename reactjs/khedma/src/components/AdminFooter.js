import React from 'react'
import './AdminNavbar.css'


const AdminFooter = (props) =>{
    return(
        <footer className="footer mt-5">
            <div className="container-fluid text-center text-md-left">
                <div className="row">
                    <div className="col-md-6 mt-md-0 mt-5">
                        <h5 className="text-uppercase">Footer Content</h5>
                        <p>Here you can use rows and columns to organize your footer content.</p>
                    </div>

                    <hr className="clearfix w-100 d-md-none pb-0"/>

                    <div className="col-md-3 mb-md-0 mb-3">
                        <h5 className="text-uppercase">Links</h5>
                        <ul className="list-unstyled">
                            <li><a href="#!">Link 1</a></li>
                            <li><a href="#!">Link 2</a></li>
                        </ul>
                    </div>

                    <div className="col-md-3 mb-md-0 mb-3">
                        <h5 className="text-uppercase">Links</h5>
                        <ul className="list-unstyled">
                            <li><a href="#!">Link 1</a></li>
                            <li><a href="#!">Link 2</a></li>
                        </ul>
                    </div>
                </div>
            </div>

            <div className="footer-copyright text-center py-3">© 2023 Copyright:
                <a href="https://khedma.site" target='_blank'> Khedma.Site</a>
            </div>

        </footer>
    )
}

export default AdminFooter;