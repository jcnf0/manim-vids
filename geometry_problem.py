from manim import *

class Graphing(Scene):
    def construct(self):
        
        self.play_title()
        x=self.play_visual()
        self.play_congruence()
        self.pause(1)
        self.play(FadeOut(x))
        self.pause(1)
        self.play_matrix()

    def play_title(self):
        title=Title("Geometry problem?")


        #text=(Tex("\\textbf{Problem : }","There are no four points in a plane ","such that ","the distance between each pair ","is an ","odd integer",".")
        text=(VGroup(Tex("\\textbf{Problem : }"),Tex("There are no four points in a plane "),Tex("such that"),Tex("the distance between each pair "),Tex("is an "),Tex("odd integer."))
        .scale(0.6)
        .arrange(RIGHT,aligned_edge=UP,buff=0.1)
        .next_to(title,DOWN,buff=0.2)
        )

        assertion=(MathTex(r"\forall a_{1},a_{2},a_{3},a_{4}\in\mathbb{R}^{2}",",",r"\exists i,j\in\{1,2,3,4\}",",",r"\forall k\in\mathbb{N},i\neq j,",r"\lVert a_{i}-a_{j}\rVert",r"\neq","2k+1")
        .next_to(text,DOWN)
        .shift(0.3*UP)
        .scale(0.6))

        self.play(FadeIn(VGroup(title)))

        self.play(Write(text))
        self.play(Write(assertion))

        #Indications
        text[1].set_color(RED)
        assertion[0].set_color(RED)
        assertion[2].set_color(RED)
        self.play(Indicate(VGroup(text[1],assertion[0],assertion[2])))
        text[3].set_color(BLUE)
        assertion[-3].set_color(BLUE)
        self.play(Indicate(VGroup(text[3],assertion[-3])))
        text[-1].set_color(GREEN)
        assertion[-1].set_color(GREEN)
        self.play(Indicate(VGroup(text[-1],assertion[-1])))



    def play_visual(self):
        plane=(NumberPlane(x_range=[-5,5,1],y_range=[-5,5,1],color=BLUE)
        .scale(0.45)
        .to_edge(DL))

        a1=Dot(point=plane.c2p(1,-1,0))
        a1_label=Tex("$(x_{1},y_{1})$").next_to(a1,UP,buff=0.1).scale(0.6)

        a2=Dot(point=plane.c2p(-1,3,0))
        a2_label=Tex("$(x_{2},y_{2})$").next_to(a2,UP,buff=0.1).scale(0.6)

        a3=Dot(point=plane.c2p(-4,-2,0))
        a3_label=Tex("$(x_{3},y_{3})$").next_to(a3,UP,buff=0.1).scale(0.6)

        a4=Dot(point=plane.c2p(-3,1,0))
        a4_label=Tex("$(x_{4},y_{4})$").next_to(a4,UP,buff=0.1).scale(0.6)

        dots=VGroup(a1,a2,a3,a4)
        dots_labels=VGroup(a1_label,a2_label,a3_label,a4_label)
        self.play(DrawBorderThenFill(plane))
        self.pause(1)
        self.play(FadeIn(dots))
        self.play(FadeIn(dots_labels))

        let_text=Tex(r"Let $a_{1},a_{2},a_{3},a_{4}\in\mathbb{R}^{2}, a_{i}\triangleq(x_{i},y_{i})$ that verify the problem.").scale(0.6).shift(2*RIGHT).shift(UP)
        self.play(Write(let_text))
        self.pause(0.5)
        supp_text=Tex(r"Suppose $a_{4}=(0,0)$ (equivalent to translating the plane)").scale(0.6).next_to(let_text,DOWN,aligned_edge=LEFT)

        self.play(Write(supp_text))

        a1prime=Dot(point=plane.c2p(4,-2,0))
        a1prime_label=Tex("$(x_{1},y_{1})$").next_to(a1prime,UP,buff=0.1).scale(0.6)
        
        a2prime=Dot(point=plane.c2p(2,2,0))
        a2prime_label=Tex("$(x_{2},y_{2})$").next_to(a2prime,UP,buff=0.1).scale(0.6)
        
        a3prime=Dot(point=plane.c2p(-1,-3,0))
        a3prime_label=Tex("$(x_{3},y_{3})$").next_to(a3prime,UP,buff=0.1).scale(0.6)

        a4prime=Dot(point=plane.c2p(0,0,0))
        a4prime_label=Tex("$(0,0)$").next_to(a4prime,UP,buff=0.1).scale(0.6)

        dots_prime=VGroup(a1prime,a2prime,a3prime,a4prime)
        dotsprime_labels=VGroup(a1prime_label,a2prime_label,a3prime_label,a4prime_label)

        self.play(Transform(dots,dots_prime),Transform(dots_labels,dotsprime_labels))

        self.play(FadeOut(let_text,supp_text))
        self.pause(1)
        return VGroup(plane,dots,dots_labels)



    def play_congruence(self):
        text1=Tex(r"Let $k\in\mathbb{N}$,",r"$(2k+1)^{2}=4k^{2}+4k+1$").scale(0.6).shift(RIGHT).shift(UP)
        text2=Tex(r"$(2k+1)^{2}=4k(1+k)+1$").next_to(text1[0],RIGHT).scale(0.6).next_to(text1[0])
        text3=Tex(r"$(2k+1)^{2}=\underbrace{4k(1+k)}_{\equiv 0 [8]}+1\equiv 1 [8]$").scale(0.6).next_to(text1[0],RIGHT,aligned_edge=UP).shift(0.1*UP)
        self.play(Write(text1))
        self.pause(0.5)
        self.play(Transform(text1[1],text2))
        self.pause(0.5)
        self.play(Transform(text1[1],text3))
        self.pause(0.5)
        text4=(VGroup(Tex(r"Since $a_{4}=(0,0),\forall i\in\{1,2,3\}\exists k\in\mathbb{N}, \lVert a_{i}-a_{4}\rVert=2k+1=\lVert a_{i}\rVert$"),
        Tex(r"Thus, $\lVert a_{i}\rVert^{2}\equiv 1[8]$"),
        Tex(r"Let $i,j\in\{1,2,3\},i\neq j$"),
        Tex(r"$\lVert a_{i}-a_{j}\rVert^{2}=\lVert a_{i}\rVert^{2}-2(a_{i},a_{j})+\lVert a_{j}\rVert^{2}$"),
        Tex(r"$\Leftrightarrow 2(a_{i},a_{j})=\lVert a_{i}\rVert^{2}+\lVert a_{j}\rVert^{2}-\lVert a_{i}-a_{j}\rVert^{2}\equiv 1[8]$"))
        .scale(0.6)
        .arrange(DOWN,aligned_edge=LEFT)
        .next_to(text1,DOWN,aligned_edge=LEFT)
        )
        text5=(Tex(r"$\boxed{2(a_{i},a_{j})\equiv 1[8]}$")
        .scale(0.6)
        .shift(5*RIGHT)
        .shift(1.5*UP)
        )

        self.play(Write(text4),run_time=5)
        self.pause(1)

        self.play(FadeOut(VGroup(text1,text3)),Transform(text4,text5))
        text5.move_to(UR)
        

    def play_matrix(self):
        Atex=(Tex(r"Let $A=\begin{bmatrix} x_{1} & x_{2} & x_{3}\\ y_{1} & y_{2} & y_{3}\end{bmatrix}$")
        .scale(0.6)
        .shift(1.5*UP)
        .shift(5*LEFT)
        )

        tAAtex=(Tex(r"$B=A^{T}A=\begin{bmatrix} x_{1} & x_{2} & x_{3}\\"+r"y_{1} & y_{2} & y_{3}\end{bmatrix}"+r"\begin{bmatrix} x_{1} & y_{1} \\ x_{2} & y_{2} \\ x_{3} & y_{3}\end{bmatrix}=\begin{bmatrix} x_{1}^{2}+y_{1}^{2} & x_{1}x_{2}+y_{1}y_{2} & x_{1}x_{3}+y_{2}y_{3} \\"+r" x_{1}x_{2}+y_{1}y_{2} & x_{2}^{2}+y_{2}^{2} & x_{2}x_{3}+y_{2}y_{3}\\"+r"x_{1}x_{3}+y_{1}y_{3} & x_{2}x_{3}+y_{2}y_{3} & c_{1}^{2}+c_{2}^{2} \end{bmatrix}$")
        .scale(0.6)
        .next_to(Atex,DOWN,aligned_edge=LEFT))

        
        B1=(Tex(r"$B=\begin{bmatrix} \lVert a_{1}\rVert^{2} & (a_{1},a_{2}) & (a_{1},a_{3})\\"+r"(a_{1},a_{2}) & \lVert a_{2}\rVert^{2} & (a_{2},a_{3})\\"+r"(a_{1},a_{3}) & (a_{2},a_{3}) & \lVert a_{3}\rVert^{2} \end{bmatrix}$")
        .scale(0.6)
        .arrange(DOWN,aligned_edge=LEFT)
        .next_to(Atex,DOWN,aligned_edge=LEFT))    

        B2=(Tex(r"$2B=\begin{bmatrix} 2\lVert a_{1}\rVert^{2} & 2(a_{1},a_{2}) & 2(a_{1},a_{3})\\"+r"2(a_{1},a_{2}) & 2\lVert a_{2}\rVert^{2} & 2(a_{2},a_{3})\\"+r"2(a_{1},a_{3}) & 2(a_{2},a_{3}) & 2\lVert a_{3}\rVert^{2} \end{bmatrix}$")        
        .scale(0.6)
        .arrange(DOWN,aligned_edge=LEFT)
        .next_to(Atex,DOWN,aligned_edge=LEFT))
        CongMat=Tex(r"$\equiv\begin{bmatrix}2 & 1 & 1\\ 1 & 2 & 1\\ 1 & 1 & 2\end{bmatrix}[8]$").scale(0.6)

        assertion=(VGroup(B2,CongMat)
        .next_to(Atex,DOWN,aligned_edge=LEFT)
        .shift(DOWN)
        .arrange(RIGHT)
        )

        text=(Tex(r"Thus, $det(2B)=\sum\limits_{\sigma\in \mathcal{S}_{3}}\epsilon(\sigma)\prod\limits_{k=1}^{3}2B_{\sigma(i),i}$")
        .scale(0.6)
        .next_to(assertion,DOWN,aligned_edge=LEFT)
        )
        
        text2=(Tex(r"Thus, $det(2B)=\sum\limits_{\sigma\in \mathcal{S}_{3}}\epsilon(\sigma)\prod\limits_{k=1}^{3}\underbrace{2(a_{\sigma(i)},a_{i})}_{\equiv 1[8]}\neq 0$")
        .scale(0.6)
        .next_to(assertion,DOWN,aligned_edge=LEFT)
        )
        
        text3=(VGroup(Tex(r"\textbf{However}, $rg(2B)=rg(B)=rg(A^{T}A)<min(rg(A^{T}),rg(A))\leq 2$"),Tex(r"Thus, $rg(B)<3$ and B isn't invertible so $det(B)=0$, \textbf{absurd}."))
        .scale(0.6)
        .arrange(DOWN,aligned_edge=LEFT)
        .next_to(assertion,DOWN,aligned_edge=LEFT)
        )
        self.play(Write(Atex))
        self.pause(2)
        self.play(Write(tAAtex))
        self.pause(1)
        self.play(Transform(tAAtex,B1))
        self.pause(2)
        self.play(Transform(tAAtex,assertion))
        self.pause(2)

        self.play(Write(text))
        self.pause(2)
        self.play(Transform(text,text2))
        self.pause(2)
        self.play(Transform(text,text3))
