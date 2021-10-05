#include <stdio.h>                                  
int r=0,x,y=0,    /*                                
nt               \ /                                
c    / \ / ||| /\_                                  
lx  /   X _ _  \ |                                  
u, ^_  / \ \/   /\                                  
dn  \           \_        ]                         
e=   \ .||  /\            =                     p p 
 0 |||   /  ||  ||        f        f       f    r r 
<,  /\          /      i  tw       t       s s  i i 
sy      <<  ||         n  eh       e       e c  n n 
t=  /\ ___  /   /\     t  li       l       e a  t t 
d0  ||      ||  \/        ll       l  {<   k n  f f 
i,             |||     tu (e s     (  fr   ( f  ( ( 
o   ||  || |     /     [[ s( t    usw o; i s (  " " 
.   -/  /   /_ |||   c222 tg rv   [th rx=f t "  % \ 
h       ||  _/   /  mh000 de{l)   +di (+'( d+%  c n+
>                   aa000 itte; > +il x+ n inc  " "+
 /                  ir000[ns[nytyrrne<=)'<xn,"  , );
 */                 n         =             0     ; 
               main        (       )   {            
                char       v   [                    
               6000    ]                   ,  s;    
         int t[6000     ]                    ,      
             u[6000               ]     ;  u        
                  [                   0             
      ]=ftell(stdin        )       ;                
         while(gets (v    )                 )       
                 {t  [         r ]=                 
             strlen                 (               
               v);y=                                
                 t[         r             ]         
                 >y             ?        t [        
                  r         ]    :   y;             
              u[++r   ]     =                       
        ftell(stdin )   ;                          }
              while          (                    n 
                  <              y        )         
            {for(x=0             ;         x        
            <r;x++) {                           s   
               = ""       ;                         
              if(n<             t        [          
                  x            ]     )    {         
        fseek(stdin    ,u       [     x    ]        
                 +n   ,  0 )                     ;  
        scanf("%c",                          &      
                                       s        )   
                   ;                             }  
       printf("%c",   s                       )     
                                            ;      }
      printf("\n");                 n               
                 ++   ;            }           }    

