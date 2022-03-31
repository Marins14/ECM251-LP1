public class Sistema {
    public void run(){
        Usuario usuario = new Usuario("Geralt", "123658", "ciri_yennefer@gmail.com");
        Conta conta = new Conta("Geralt", 1234);

        System.out.println(conta);
        Transacoes steam = new Transacoes(200,usuario); 
        
        conta.depositar(300);
        

    }
    boolean pagarQRcode(Transacoes qrcode, Conta conta){
        double valorPagar;
        
            valorPagar = qrcode.getValor();
        
            return true;
        
        
    } 
        
    
}
