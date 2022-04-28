// Matheus Marins Bernardello
// RA: 20.00286-6
public class Aplicacao {
    public static void run(){
        Usuario usuario1 = new Usuario("Geralt");
        Usuario usuario2 = new Usuario("Triss");
        Usuario usuario3 = new Usuario("Vesemir");
        Usuario usuario4 = new Usuario("Yennefer");
        Usuario usuario5 = new Usuario("Ciri");

        System.out.println("Usuario e bens associados:" + usuario1 + usuario1.getBens().testar());
        System.out.println("Usuario e bens associados:" + usuario2 + usuario2.getBens().testar());
        System.out.println("Usuario e bens associados:" + usuario3 + usuario3.getBens().testar());
        System.out.println("Usuario e bens associados:" + usuario4 + usuario4.getBens().testar());
        System.out.println("Usuario e bens associados:" + usuario5 + usuario5.getBens().testar());


       
    }
}
