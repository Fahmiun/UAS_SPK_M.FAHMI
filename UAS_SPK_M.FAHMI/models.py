from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class tbl_hp(Base):
    __tablename__ = 'tbl_hp'
    hp: Mapped[str] = mapped_column(primary_key=True)
    harga: Mapped[int] = mapped_column()
    ram: Mapped[int] = mapped_column()
    kapasitas_baterai: Mapped[int] = mapped_column()
    processor: Mapped[int] = mapped_column()
    penyimpanan_internal: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
        return f"tbl_hp(hp={self.hp!r}, harga={self.harga!r})"