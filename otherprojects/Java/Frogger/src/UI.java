import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import java.awt.geom.Line2D.Double;

public class UI extends JPanel implements ActionListener,KeyListener
{
	Timer t = new Timer(5,this);
	double xBus = 0, velXBus = 2;
	double xPlr = 0, yPlr = 0, velXPlr = 0, velYPlr = 0;
	
	public UI()
	{
		t.start();
		addKeyListener(this);
		setFocusable(true);
		setFocusTraversalKeysEnabled(false);
	}
	public void paintComponent(Graphics g)
	{
		super.paintComponent(g);
		Graphics2D g2 = (Graphics2D) g;
		int TOTALLINES = 6;
		
		for(int line = 0; line < TOTALLINES;line++)
		{
			Line2D forAddLine = new Line2D.Double(0,100 + line*100,
					600,100 +line*100);
			g2.draw(forAddLine);
		}
		
		Ellipse2D oval = new Ellipse2D.Double(xPlr,yPlr + 600,50,50);
		g2.setPaint(Color.BLUE);
		g2.fill(oval);
		
		Rectangle2D bus = new Rectangle2D.Double(xBus-200,100,200,100);
		g2.setPaint(Color.RED);
		g2.fill(bus);
		
		Rectangle2D bus2 = new Rectangle2D.Double(600-xBus,200,200,100);
		g2.setPaint(Color.GREEN);
		g2.fill(bus2);
	}

	public void actionPerformed(ActionEvent e)
	{
		xBus += velXBus;
		xPlr += velXPlr;
		yPlr += velYPlr;
		repaint();
	}
	public void up()
	{
		velYPlr = -1.5;
	}
	public void down()
	{
		velYPlr = 1.5;
	}
	public void left()
	{
		velXPlr = -1.5;
	}
	public void right()
	{
		velXPlr = 1.5;
	}
	public void keyPressed(KeyEvent e)
	{
		int code = e.getKeyCode();
		if(code == KeyEvent.VK_UP)
		{
			up();
		}
		if(code == KeyEvent.VK_DOWN)
		{
			down();
		}
		if(code == KeyEvent.VK_RIGHT)
		{
			right();
		}
		if(code == KeyEvent.VK_LEFT)
		{
			left();
		}
	}
	public void keyReleased(KeyEvent e)
	{
		int code = e.getKeyCode();
		if(code == KeyEvent.VK_UP)
		{
			velYPlr = 0;
		}
		if(code == KeyEvent.VK_DOWN)
		{
			velYPlr = 0;
		}
		if(code == KeyEvent.VK_RIGHT)
		{
			velXPlr = 0;
		}
		if(code == KeyEvent.VK_LEFT)
		{
			velXPlr = 0;
		}
	}
}
