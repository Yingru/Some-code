cccccccccccccccccccccccccccccccccccccccccccccccccc
c
c  standard common block 
c 


      integer  NT, NX, NY, NZ
      parameter (NT = 5)
      parameter (NX = 77)
      parameter (NY = 77)
      parameter (NZ = 32)

      double precision, dimension(1:NT, -NX:NX, -NY:NY, -NZ:NZ) :: posi_x, posi_y, Rap, Vx, Vy, Vz, Energy, TJT, TJAT
      common /hydro_info/ posi_x, posi_y, Rap, Vx, Vy, Vz, Energy, TJT, TJAT

     
       
      

