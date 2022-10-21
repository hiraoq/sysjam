import { Button, Card, CardContent, ListItem } from "@mui/material";
import { Container } from "@mui/system";
import { NextPage } from "next";
import Link from "next/link";
import { useEffect, useState } from "react";
import Layout from "../../components/Layout";

const Comic: NextPage = () => {
  type Comic = {
    author: String;
    title: String;
  };

  const [comics, setComics] = useState<Comic[]>([]);
  const [counts, setCounts] = useState(0);

  useEffect(() => {
    fetch("/api/comics")
      .then((r) => r.json())
      .then((data: Comic[]) => setComics(data));
  }, []);

  return (
    <Container>
      <Button>show comics</Button>
      {comics.map((comic) => (
        <Card>
          {comic.title} : {comic.author}
        </Card>
      ))}
    </Container>
  );
};

export default Comic;
