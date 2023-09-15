class A:
  def _method(self) -> None:
    print('Initial method')

  def post(self):
    self._method()


class B(A):
  def _method(self) -> None:
    print('Method overrided from B')


class C(A):
  def _method(self) -> None:
    print('Method overrided from C')


class D(B):
  def _method(self) -> None:
    print('Method from B overrided from D')


a = A()
b = B()
c = C()
d = D()

a.post()
b.post()
c.post()
d.post()
