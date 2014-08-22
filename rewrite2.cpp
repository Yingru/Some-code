void CHydro3D::Output(const int & NT)
{
    char fbuf[256];
    sprintf(fbuf, "%s/results/event%d/output.dat", HOME, IEVENT);
    ofstream f_data(fbuf, ios::app);
    
    char fbuf2[256];
    sprintf(fbuf2, "%s/results/event%d/Anisotropy.dat", HOME, IEVENT);
    ofstream f_ecc(fbuf2, ios::app);
    
    cout<<"time="<<tau<<"\n";
    cout<<"After evolution Ed="<<"\n";
    for (int I=0; I<=NX; I+=10)
    {
        for (int J=0; J<=NY; J+=10)
        {
            cout<<setw(15)<<Ed(I,J,0);
        }
    }
    
    f_data<<"#tau="<<tau<<"\n";
    f_data<<"#      x       y       rapidity        energy density";
    
    for (i=NX0; i<=NX; i++)
    {
        for (j=NY0; j<=NY; j++)
        {
            for (k=NZ0; k<=NZ; k++)
            {
                f_data<<setprecision(8)<<setw(20)<<dx*i<<setw(20)<<dy*j<<setw(20)<<dz*k<<setw(20)<<Vx(i,j,k)<<setw(20)<<Vy(i,j,k)<<setw(20)<<Vz(i,j,k)*tau<<setw(20)<<Ed(i,j,k)<<setw(20)<<TJT(i,j,k)<<setw(20)<<TJAT(i,j,k)<<"\n";
            }
        }
    }
    
    double epsx, epsp;
    Accecentricity(espx, esps);
    f_ecc<<"#tau="<<tau<<"\n";
    f_ecc<<setprecision(8)<<setw(20)<<espx<<setw(20)<<esps<<"\n";
    
    
    f_data.close();
    f_ecc.close();
    
}   //End of output 
    //Now still have problem about how to get rid of NT??(It seems like I have get rid of NT already)
    



