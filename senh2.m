function [senh]=senh2(x)
    tmp = x;
    x=abs(x);
    E=exp(x)-1;
    lnovft=log(realmax);
    ln2ovft=log(2)+lnovft;
    
        if 0<=x && x<=22
            senh= (E+E./(E+1))./2;
        end

        if 22<x && x<=lnovft
            senh=exp(x)./2;
        end

        if lnovft<x && x<=ln2ovft
            senh=exp(x./2)./2*exp(x./2);
        end

        if ln2ovft<x
            disp('Si è andati in overflow');
        end
        
        if tmp < 0
          senh = -senh;
        end
end
