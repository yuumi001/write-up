#include <stdio.h>                                   
int x,n=0,y=0,    /*                                 
nt                 /                                 
c    ^  |                                            
lr  /_\ |/ /| |-                                     
u= /   \|\ \| |/                                     
d0                        ]                       p  
e, \ / .   _              =                     p r  
 x  X  |  <_  |/|         f        f       f s  r i  
<, / \ |/ <_  | |      i  tw       t       s c  i n  
sy  _                  n  eh       e       e a  n t  
t= | \        |        t  li       l       e n  t f  
d0 |_/ /| |/|  /_         ll       l  {<   k f  f (  
i, |   \| | |  _/      tu (e s     (  fr   ( (  ( "  
o                      [[ s( t    usw o; i s "  " \  
.  /\        | |    m 222 tg rv   [th rx=f t %  % n  
h  \ /\ |/ /\| |    ac000 de l)   +di (+'( d c  c "  
> \_|\_ |  \/|/|/   ih000 it{e;t> +il x+ n i+"  " )+ 
 /                  na000[nstny[yrrne<=)'<xnn,  , ;+ 
 */                  r        =       0        ;     
                main       (       )   {             
               char        v[                        
               2000               ]         ,   s  ; 
         int t[2000   ]                    ,         
             u[2000    ]           ;       u         
                  [                         0        
      ]=ftell(stdin        )            ;            
         while(gets (v    )                 )        
                {t[            r ]=                  
             strlen                 (                
               v);y=                                 
                  t  [      r             ]          
                 >y             ?        t [         
                  r         ]    :   y;              
              u[++r     ]   =                        
        ftell(stdin )     ;                        } 
              while          (                    n  
                  <              y        )          
            {for(x=      0       ;         x         
            <r;x++) {                         s      
               =' '     ;                            
              if(n<             t        [           
                  x            ]     )    {          
        fseek(stdin   , u       [     x    ]         
                +n,0       )                     ;   
         scanf("%c"    ,                     &       
                      s                         )    
                      ;                            } 
       printf("%c",                    s      )      
                                            ;  }     
       printf("\n");                n                
                ++;                }             }   
