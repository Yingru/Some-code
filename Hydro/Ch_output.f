      subroutine hydro_output_backup(t0, x0, y0, z0, betax, betay, betaz, Energy0, TJT0, TJA0)

      implicit none
      include 'ucom.f'

      double precision:: t0, x0, y0, z0, h_vx, h_vy, h_veta, Energy0, TJT0, TJAT0, tau, h_reta, betax, betay, betaz, T
      integer:: ti, xi, yi, zi

c    change the input coordinate from x(t, x, y, z) tp X(tau, x, y, h_reta)
      tau=sqrt(t0*t0-z0*z0)
      h_reta=0.5d0*dLOG((t0+z0)/(t0-z0))


c    point out the nearest grid around our input position
      ti=INT((tau-0.64)/dt)+1

      if (x0 .gt. 0) then
          xi=INT(x0/dx)
      else
          xi=INT(x0/dx)-1

      if (y0 .gt. 0) then
          yi=INT(y0/dy)
      else
          yi=INT(y0/dy)-1

      if (h_reta .gt. 0) then
          zi=INT(h_reta/dz)
      else
          zi=INT(h_reta/dz)-1


      fx=(x0-xi*dx)/dx
      fy=(y0-yi*dy)/dy
      fz=(h_reta-zi*dz)/dz
      dt=(tau-ti*dt)/dt

c     get the (Vx=h_vx, Vy=h_vy, Vz=h_veta, T) of input position in coordinate X(tau, x, y, h_reta)
      h_vx=Vx(ti, xi, yi, zi)*(1-ft*(1-fz*(1-fy*(1-fx))))+Vx(ti, xi, yi, zi)*ft*(1-fz*(1-fy*(1-fx)))+(Vx(ti+1, xi, yi, zi+1)-Vx(ti, xi, yi, zi+1))*ft*fz*(1-fy*(1-fx))+(Vx(ti+1, xi, yi+1, zi+1)-Vx(ti+1, xi, yi+1, zi)-Vx(ti, xi, yi+1, zi+1)+Vx(ti, xi, yi+1, zi))*ft*fz*fy*(1-fx)+(Vx(ti+1, xi+1, yi+1, zi+1)-Vx(ti+1, xi+1, yi, zi+1)-Vx(ti+1, xi+1, yi+1, zi)+Vx(ti+1, xi+1, yi, zi+1)-Vx(ti, xi+1, yi+1, zi+1)+Vx(ti, xi+1, yi, zi+1)+Vx(ti, xi+1, yi+1, zi)-Vx(ti, xi+1, yi, zi+1))*ft*fz*fy*fx

      h_vy=Vy(ti, xi, yi, zi)*(1-ft*(1-fz*(1-fy*(1-fx))))+Vy(ti, xi, yi, zi)*ft*(1-fz*(1-fy*(1-fx)))+(Vy(ti+1, xi, yi, zi+1)-Vy(ti, xi, yi, zi+1))*ft*fz*(1-fy*(1-fx))+(Vy(ti+1, xi, yi+1, zi+1)-Vy(ti+1, xi, yi+1, zi)-Vy(ti, xi, yi+1, zi+1)+Vy(ti, xi, yi+1, zi))*ft*fz*fy*(1-fx)+(Vy(ti+1, xi+1, yi+1, zi+1)-Vy(ti+1, xi+1, yi, zi+1)-Vy(ti+1, xi+1, yi+1, zi)+Vy(ti+1, xi+1, yi, zi+1)-Vy(ti, xi+1, yi+1, zi+1)+Vy(ti, xi+1, yi, zi+1)+Vy(ti, xi+1, yi+1, zi)-Vy(ti, xi+1, yi, zi+1))*ft*fz*fy*fx

      h_veta=Vz(ti, xi, yi, zi)*(1-ft*(1-fz*(1-fy*(1-fx))))+Vz(ti, xi, yi, zi)*ft*(1-fz*(1-fy*(1-fx)))+(Vz(ti+1, xi, yi, zi+1)-Vz(ti, xi, yi, zi+1))*ft*fz*(1-fy*(1-fx))+(Vz(ti+1, xi, yi+1, zi+1)-Vz(ti+1, xi, yi+1, zi)-Vz(ti, xi, yi+1, zi+1)+Vz(ti, xi, yi+1, zi))*ft*fz*fy*(1-fx)+(Vz(ti+1, xi+1, yi+1, zi+1)-Vz(ti+1, xi+1, yi, zi+1)-Vz(ti+1, xi+1, yi+1, zi)+Vz(ti+1, xi+1, yi, zi+1)-Vz(ti, xi+1, yi+1, zi+1)+Vz(ti, xi+1, yi, zi+1)+Vz(ti, xi+1, yi+1, zi)-Vz(ti, xi+1, yi, zi+1))*ft*fz*fy*fx

      Energy0=Energy(ti, xi, yi, zi)*(1-ft*(1-fz*(1-fy*(1-fx))))+Energy(ti, xi, yi, zi)*ft*(1-fz*(1-fy*(1-fx)))+(Energy(ti+1, xi, yi, zi+1)-Energy(ti, xi, yi, zi+1))*ft*fz*(1-fy*(1-fx))+(Energy(ti+1, xi, yi+1, zi+1)-Energy(ti+1, xi, yi+1, zi)-Energy(ti, xi, yi+1, zi+1)+Energy(ti, xi, yi+1, zi))*ft*fz*fy*(1-fx)+(Energy(ti+1, xi+1, yi+1, zi+1)-Energy(ti+1, xi+1, yi, zi+1)-Energy(ti+1, xi+1, yi+1, zi)+Energy(ti+1, xi+1, yi, zi+1)-Energy(ti, xi+1, yi+1, zi+1)+Energy(ti, xi+1, yi, zi+1)+Energy(ti, xi+1, yi+1, zi)-Energy(ti, xi+1, yi, zi+1))*ft*fz*fy*fx

      TJT0=TJT(ti, xi, yi, zi)*(1-ft*(1-fz*(1-fy*(1-fx))))+TJT(ti, xi, yi, zi)*ft*(1-fz*(1-fy*(1-fx)))+(TJT(ti+1, xi, yi, zi+1)-TJT(ti, xi, yi, zi+1))*ft*fz*(1-fy*(1-fx))+(TJT(ti+1, xi, yi+1, zi+1)-TJT(ti+1, xi, yi+1, zi)-TJT(ti, xi, yi+1, zi+1)+TJT(ti, xi, yi+1, zi))*ft*fz*fy*(1-fx)+(TJT(ti+1, xi+1, yi+1, zi+1)-TJT(ti+1, xi+1, yi, zi+1)-TJT(ti+1, xi+1, yi+1, zi)+TJT(ti+1, xi+1, yi, zi+1)-TJT(ti, xi+1, yi+1, zi+1)+TJT(ti, xi+1, yi, zi+1)+TJT(ti, xi+1, yi+1, zi)-TJT(ti, xi+1, yi, zi+1))*ft*fz*fy*fx

      TJAT0=TJAT(ti, xi, yi, zi)*(1-ft*(1-fz*(1-fy*(1-fx))))+TJAT(ti, xi, yi, zi)*ft*(1-fz*(1-fy*(1-fx)))+(TJAT(ti+1, xi, yi, zi+1)-TJAT(ti, xi, yi, zi+1))*ft*fz*(1-fy*(1-fx))+(TJAT(ti+1, xi, yi+1, zi+1)-TJAT(ti+1, xi, yi+1, zi)-TJAT(ti, xi, yi+1, zi+1)+TJAT(ti, xi, yi+1, zi))*ft*fz*fy*(1-fx)+(TJAT(ti+1, xi+1, yi+1, zi+1)-TJAT(ti+1, xi+1, yi, zi+1)-TJAT(ti+1, xi+1, yi+1, zi)+TJAT(ti+1, xi+1, yi, zi+1)-TJAT(ti, xi+1, yi+1, zi+1)+TJAT(ti, xi+1, yi, zi+1)+TJAT(ti, xi+1, yi+1, zi)-TJAT(ti, xi+1, yi, zi+1))*ft*fz*fy*fx


c     ask exactly what is the form of calculate temperature

c     change coordinate from (h_vx, h_vy, h_veta, T) to (betax, betay, betaz, T)

      TMP=0.5d0*dLOG((1+h_veta)/(1-h_veta))+h_reta

      betax=h_vx*DCOSH(TMP-h_reta)/DCOSH(TMP)
      betay=h_vy*DCOSH(TMP-h_reta)/DCOSH(TMP)
      betaz=(h_veta+DTANH(h_reta))/(1+h_veta*DTANH(h_reta))


      return
      end

