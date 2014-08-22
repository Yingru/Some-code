program raa
 implicit none
 
 double precision, dimension(1:1000):: ptbin,ptbinpp
 double precision:: px,py,pz,E,ptrans,rap
 integer:: i,dummy,ipt,ptsum,ptsumpp

 ptsum=0
 ptbin=0

 open(unit=10, file='test2.dat')
 read(10,*) 
 read(10,*) 
 do i=1,29 
    read(10,*) px,py,pz,dummy,dummy,dummy,E,dummy,dummy
    ptrans=sqrt(px*px+py*py) 
    rap=0.5*log((E+pz)/(E-pz))
    if(ptrans<50.0d0) then

    ipt=int(ptrans/0.5d0)+1
    ptbin(ipt)=ptbin(ipt)+1/0.5d0
    ptsum=ptsum+1
    endif
enddo
close(10)

 ptsumpp=0
 ptbinpp=0

 open(unit=10, file='test2.dat')
 read(10,*) 
 read(10,*) 
 read(10,*) 
 read(10,*) 
 do i=1,200000 
    read(10,*) px,py,pz,dummy,dummy,dummy,E,dummy,dummy
    ptrans=sqrt(px*px+py*py) 
    rap=0.5*log((E+pz)/(E-pz))
    if(ptrans<50.0d0) then

    ipt=int(ptrans/0.5d0)+1
    ptbinpp(ipt)=ptbinpp(ipt)+1/0.5d0
    ptsumpp=ptsumpp+1
    endif
enddo
close(10)

open(unit=11, file='dNdpT_pp_pPb.dat')


 do i=1,1000
    ptrans=(i+1)*0.5d0
    write(11,*) ptrans, ptbin(i)/ptsum,ptbinpp(i)/ptsumpp
 enddo

end
