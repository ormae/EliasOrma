import javax.swing.*;
import java.awt.*;

public class ikkuna extends JFrame{

	public ikkuna()
	{
		setTitle("ikkuna");
		setSize(600,735);		
		setVisible(true);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setResizable(false);
		
	}
public static void main(String[] args)
	{
		
		ikkuna a = new ikkuna();
		UI r = new UI();
		//auto car = new auto();
		a.add(r);
	}
}
